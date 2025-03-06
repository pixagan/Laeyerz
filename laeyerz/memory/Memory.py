# Created: Anil Variyar
# Memory

from laeyerz.memory.VectorDB import VectorDB
from laeyerz.memory.NoSql import NoSql
from laeyerz.memory.GraphDB import GraphDB

from laeyerz.embeddings.EmbeddingModel import EmbeddingModel
import uuid


class Memory:

    def __init__(self, config):
        print("Initializing Memory")

        self.vectorDB       = VectorDB(config["VectorDB"], config["VectorDB_Params"])
        
        self.embeddingModel = EmbeddingModel(config["EmbeddingModel"]["vendor"], config["EmbeddingModel"]["model_name"])

        self.nosql          = NoSql(config["NoSQL"])

        self.memGraph       = GraphDB(config["GraphDB"])
        
    


    def load_session_list(self):
        print("Loading Session List")

        session_list = list(self.nosql.load_session_list())

        return session_list


    def add_session(self, title):
        print("Adding Session")

        session_id = str(uuid.uuid4())

        isCreated = self.nosql.create_session(session_id, title)

        return isCreated



    def add_session_item(self, session_id, item):

        self.nosql.add_session_item(session_id, item)
        

    def load_session(self, title):
        print("Loading Session")

        curr_session = self.nosql.load_session(title)

        return curr_session



    def load_session_history(self, session_id):
        print("Loading Session History")

        self.nosql.load(session_id)



    def add_document(self, document, document_type):
        print("Adding Document")

        document_id = str(uuid.uuid4())

        self.nosql.create_document(document_id, document['title'], document['type'])


        texts = []
        
        for chunk in document['chunks']:
            chunk['document_id'] = document_id
            chunk['id'] = str(uuid.uuid4())
            texts.append(chunk['text'])

        
        self.nosql.add_items(document["chunks"])

        embeddings = self.embeddingModel.encode(texts)

       

        metadata = [{'document_id': document_id, 'text': chunk['text'], 'id': chunk['id']} for chunk in document['chunks']] 

        self.vectorDB.store(embeddings, metadata)

        


    def combine_memories(self, memories):
        print("Combining Memories")

        #combine the memories into a single string

        combined_memories = ""

        for memory in memories:
            #print("Memory : ",memory)
            combined_memories += memory['metadata']['text'] + "\n"
        
        return combined_memories



    def search(self, session_id, query):
        print("Run")

        #text to embedings
        query_embedding = self.embeddingModel.encode(query['query'])
        memories        = self.vectorDB.search(query_embedding)

        #search the graph for relevant memories
        combined_memories = self.combine_memories(memories)
        

        return combined_memories


        





#----------------------------------------------------------------------




def main():

    mem = Memory()
   

#----------------------------------------------------------------------

if __name__ == "__main__":
    main()


#----------------------------------------------------------------------
