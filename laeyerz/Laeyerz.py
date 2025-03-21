# Created: Anil Variyar
# Laeyerz

import os
from dotenv import load_dotenv
load_dotenv()

from datetime import datetime

from laeyerz.memory.Memory import Memory
from laeyerz.llms.LLMx import LLMx
from laeyerz.LDocument import LDocument

#from KeyManager import KeyManager

templatepath = os.getenv('TEMPLATE_PATH')
filepath     = os.getenv('FILE_PATH')


class LaeyerzConfig:

    def __init__(self, config):
        print("Config")

        if(not config):
            config =self.default()
        else:

            self.appname = 'App 1'
            self.LLM = config_id['LLM']
            self.VectorDB = config_id['VectorDB']
            self.VectorDB_params = {
                "index_name": config_id['VectorDB_index_name'],
            }

            self.EmbeddingModel = config_id['EmbeddingModel']
            self.NoSQL = config_id['NoSQL']
            self.GraphDB = config_id['GraphDB']


    def default():
        return {
            "appname": "App 1",
            "LLM": "gpt-4o",
            "VectorDB": "Pinecone",
            "VectorDB_params": "index_name",
            "EmbeddingModel": "OpenAI",
        }


    def load_config(self, config_id):   
        print("Loading config")

        config = Config(config_id)
        return config

    def write_config(self, config_id, text):

        config = Config(config_id)
        return config



class Session:

    def __init__(self, session_id, memory, llm):
        print("A Chat Session")
        #for each session have a set of keys that can be checked  for existenace
        self.session_id = session_id
        self.title      = ""
        self.memory     = memory
        self.llm        = llm

    def setup(self, config):
        print("Setting up session")


    def load_history(self, session_id):
        print("Loading session")
        
        self.memory.load_session_history(self.session_id)


    def chat(self, query):

        #load the memories
        memories = self.memory.search(self.session_id, query)

        #use the llm to improve on the conversation

        start_time = datetime.now()
        
        llm_response = self.llm.run(query["instructions"], query["query"], memories, params={})

        llm_response["session_id"] = self.session_id
        llm_response["instruction"] = query["instructions"]
        llm_response["query"] = query["query"]

        end_time = datetime.now()

        llm_response["start_time"] = start_time.isoformat()
        llm_response["end_time"] = end_time.isoformat()

        

        self.memory.add_session_item(self.session_id, llm_response)

        return llm_response





class Laeyerz:

    def __init__(self, config=None):
        print("Layers")
        #self.keys     = KeyManager()
        self.memory   = Memory(config)
        self.llm      = LLMx(config['LLM'])

        #self.config   = Config(config)
        

    def setup(self, config):
        print("Setting up steps")





    def add_document(self, document, document_type):
        print("Adding document")

        self.memory.add_document(document, document_type)

        return document


    def load_session_list(self):
        print("Loading session list")

        session_list = self.memory.load_session_list()

        return session_list


    def create_session(self, title):
        print("Creating session")

        isCreated = self.memory.add_session(title)

        if(isCreated):
            curr_session = self.load_session(title)

            return curr_session

        else:
            print("Session already exists! Session titles should be unique")
            return False


    def load_session(self, title):
        print("Setting session")

        curr_session = self.memory.load_session(title)

        loaded_session = Session(curr_session['id'], self.memory, self.llm)
        
        return loaded_session



    def load_document(self, document_id):
        print("Loading document")

        document = Document(document_id)
        return document



    def load_config(self, config_id):
        print("Loading config")

        config = Config(config_id)
        return config


    def write_config(self, session_id, text):
        print("Writing session")

        session = Session(session_id, self.memory, self.llm)
        return session



#----------------------------------------------------------------------


def main():

    #laeyers
    config = {
        "appname": "Example 1",
        "LLM": {"vendor": "OpenAI", "model": "gpt-4o"},
        "VectorDB": "Pinecone",
        "VectorDB_Params":{
            "index_name": "example2-index",
            "namespace": "example2-namespace",
            "dimension": 384,
            "metric": "cosine",
            "spec": "serverless"
        },
        "EmbeddingModel": {"vendor": "HuggingFace", "model_name": "paraphrase-MiniLM-L6-v2"},
        "NoSQL": "Mongo",
        "GraphDB": "None"
    }

    #Setup a Laeyerz Instance
    ly = Laeyerz(config)

   
    


#----------------------------------------------------------------------

if __name__ == "__main__":
    main()


#----------------------------------------------------------------------

     