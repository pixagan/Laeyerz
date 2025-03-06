#Created: Anil Variyar
# A Document

import os
import numpy as np
from fileio.PdfLoad import PdfLoad
from textsplitters.TextSplitter import TextSplitter
from databases.PineconeAdapter import PineconeAdapter
from embeddings.SentenceTransformerAdapter import SentenceTransformerAdapter
from vectorindex.FAISSIndex import FaissIndex

from dotenv import load_dotenv
load_dotenv()

filepath = os.getenv('FILE_PATH')
pc_index = os.getenv('PC_INDEX')

#Document Memory is where all the Databasing and search happens
class DocumentTemporary:

    def __init__(self):
        self.memory = FaissIndex(384)


    def load_document(self, file):
        self.memory.load(file)

    
    def new_document(self, vectors):
        vectors = np.array(vectors).astype('float32')
        self.memory.generate(vectors)


    def search(self, query):
        distances, indices = self.memory.search(query)



class DocumentMemory:

    def __init__(self):
        print("Document Memory")
        self.embedding_model = None
        self.vector_db       = PineconeAdapter()
        self.nosql           = MongoAdapter()


    def load_document(self, file):
        self.faiss.load(file)


    def new_document(self, vectors):

        vectors = np.array(vectors).astype('float32')
        self.faiss.generate(vectors)
        

    def search(self, query):
        distances, indices = self.faiss.search(query)





class Document:

    def __init__(self, memory):
        print("Memory X")
        self.title  = None
        self.memory = memory


    def add(self, document, document_type):
        print("Adding document")

        items = None
        with open(filename, 'r') as file:
            items = json.load(file)

        print("Document : ", items)

        if(items):
            for item in items:
                self.memory.add(item, item_type)


    def setup(self):
        print("Setup")


    def load(self):
        self.memory.load()


    def upload_data(self, data):

        text = data

        #chunks = self.generate_chunks(text)

        chunks = text

        embeddings = self.embeddingModel.run(chunks)

        self.memory_st.new_document(embeddings)



    def upload_file(self, filename, filetype):
        print("Loading a Document by filename")

        if(filetype == 'text'):
            text = PdfLoad().run(filename)

        elif(filetype == 'pdf'):
            text = PdfLoad().run(filename)



        chunks = self.generate_chunks(text)
        
        embeddings = self.embeddingModel.run(chunks)

        self.memory.add(embeddings)

        

    def generate_chunks(self, text):

        chunks = TextSplitter().run(text)

        return chunks



    def store(self):
        print("Updating Agent Memory")



    def chat(self, text_in):
        print("Searching Agent Memory")

        #get memories from document
        mem_out = self.memory.search(text_in)

        print("Mem out ", mem_out)

        response = None

        return response


    def export_file(self, filename):
        print("Export File")




#----------------------------------------------------------------------




def main():

    document1 = Document()
   

 



#----------------------------------------------------------------------

if __name__ == "__main__":
    main()


#----------------------------------------------------------------------

     