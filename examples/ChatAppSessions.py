from laeyerz.flow.Flow import Flow
from laeyerz.flow.Node import Node
from laeyerz.flow.Edge import Edge
from laeyerz.flow.Model import Model

#importing the models
from laeyerz.utils.KeyManager import KeyManager

#from laeyerz.tools.TextInput import TextInput

from laeyerz.llms.Prompt import Prompt
from laeyerz.llms.LLMx import LLMx

from laeyerz.embeddings.EmbeddingModel import EmbeddingModel
from laeyerz.memory.VectorStore import VectorStore

from laeyerz.tools.DataParser import DataParser
#from laeyerz.tools.TextOutput import TextOutput
from laeyerz.LaeyerzApp import LaeyerzApp


import numpy as np

#Load the Keys for the Different Components - .env
keys = KeyManager()


#Setup the Components -----
embedding   = EmbeddingModel()
memory      = VectorStore('Pinecone', {
            "index_name": "example2-index",
            "namespace": "example2-namespace",
            "dimension": 384,
            "metric": "cosine",
            "spec": "serverless"
        })
prompt      = Prompt()
llm         = LLMx({"vendor": "OpenAI", "model": "gpt-4o"})
data_parser = DataParser()
#--------- Nodes --------------------

#Extracts text from input and stores it in the AppState

# Input node
def chat_input_function(app_state, args={}):

    query        = app_state["query"]
    instructions = input_data["instructions"]

    app_state["Query"]        = query
    app_state["Instructions"] = instructions



# Embedding node
def embedding_function(app_state, args={}):

    text_input = app_state.get_params(["Query"])

    print("Query: ",text_input)
    
    output = embedding.encode([text_input["Query"]])

    app_state.set_state("Query_Embeddings",output[0])

    print("Query_Embeddings: ",output)
    
    return app_state



# Vector DB node
def search_vectorbd(app_state, args={}):
    embedding = app_state.get_params(["Query_Embeddings"])
    
    embedding_vector = np.array(embedding["Query_Embeddings"])

    output = memory.search(embedding_vector)
    app_state.set_state("Memories",output)
    return app_state




# Prompt node
def prompt_function(app_state, args={}):
    
    inputs = app_state.get_params(["Instructions", "Query", "Memories"])
    prompt = prompt.create(inputs)
    app_state.set_state("Prompt",prompt)

    return app_state




# LLM node
def llm_function(app_state, args={}):
    
    #inputs = app_state.get(["Prompt"])
    inputs = app_state.get_params(["Instructions", "Query", "Memories"])

    instructions = inputs["Instructions"]
    query        = inputs["Query"]
    memories     = inputs["Memories"]

    print("LLM Inputs ", inputs)

    #outputs     = llm.evaluate(inputs)
    llm_response = llm.run(instructions, query, memories, params={})
        #construct the prompt

    print("LLM Response: ",llm_response)

    app_state.set_state("LLM_OUTPUT",llm_response["response"])


    app_state.set_state("Outputs",llm_response["response"])

    return app_state





# Data Parser node
def data_parser_function(app_state, args={}):    
    inputs = app_state.get_params(["LLM_OUTPUT"])
    
    outputs = data_parser.evaluate(inputs)
    app_state.set_state("DataParser",outputs)
    return app_state




# Text Output node
def text_output_function(app_state, args={}):
    inputs = app_state.get_params(["DataParser"])
    #text_output = TextOutput()
    #outputs = text_output.evaluate(inputs)
    app_state.set_state("App_Output",inputs)
    return app_state




#Initializing the RAG flow ---------------------------------
rag_flow = Flow()



#--------- Nodes ------------------------------

#rag_flow.add_node("Chat_Input", chat_input_function)
rag_flow.add_node("Embedding_Model", embedding_function)
rag_flow.add_node("Vector_DB", search_vectorbd)
#rag_flow.add_node("Prompt", prompt_function)
rag_flow.add_node("LLM", llm_function)
rag_flow.add_node("DataParser", data_parser_function)
#rag_flow.add_node("TextOutput", text_output_function)

#------ Edges --------------------

#rag_flow.add_edge("START", "Chat_Input")
rag_flow.add_edge("START", "Embedding_Model")
rag_flow.add_edge("Embedding_Model", "Vector_DB")

#rag_flow.add_edge("Vector_DB", "Prompt")
#rag_flow.add_edge("Prompt", "LLM")

rag_flow.add_edge("Vector_DB", "LLM")
rag_flow.add_edge("LLM", "END")

#rag_flow.add_edge("LLM", "DataParser")
#rag_flow.add_edge("DataParser", "END")
#rag_flow.add_edge("TextOutput", "END")


#Finalize/Freeze your Flow before evaluation
rag_flow.finalize()


#based on the input node  
input_data = {   
        "Instructions":"Respond to the user's query based on the provided information.",
        "Query":"What are the applications of RAG?"
}


output = rag_flow.evaluate(input_data)
print("RAG : ",output)



LaeyerzApp.run()
#---------