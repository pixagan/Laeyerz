from laeyerz.memory.Memory import Memory
from laeyerz.llms.LLMx import LLMx
from laeyerz.LDocument import LDocument

class Conversations:

    def __init__(self, session_id, title, memory, llm):
        print("A Chat Session")
        #for each session have a set of keys that can be checked  for existenace
        self.session_id = session_id
        self.title      = title
        self.memory     = memory
        self.llm        = llm


    def setup(self, config):
        print("Setting up session")


    def load_history(self):
        print("Loading session")
        
        items = self.memory.load_session_history(self.session_id)

        print("Chats : ", items)

        return items


    def chat(self, query):

        #load the memories
        memories = self.memory.search(self.session_id, query)

        #use the llm to improve on the conversation

        start_time = datetime.now()
        
        llm_response = self.llm.run(query["instructions"], query["query"], memories, params={})

        llm_response["session_id"]  = self.session_id
        llm_response["instruction"] = query["instructions"]
        llm_response["query"]       = query["query"]

        end_time = datetime.now()

        llm_response["start_time"] = start_time.isoformat()
        llm_response["end_time"]   = end_time.isoformat()

        

        self.memory.add_session_item(self.session_id, llm_response)


        print("LLM Response : ", llm_response)


        return llm_response




#----------------------------------------------------------------------


def main():

   conv1 = Conversations("conv1", "Conversation 1", "memory1", "llm1")

   
    


#----------------------------------------------------------------------

if __name__ == "__main__":
    main()


#----------------------------------------------------------------------

     

