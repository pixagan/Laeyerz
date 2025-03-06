# Created: Anil Variyar
# Quickstart RAG

from laeyerz.Laeyerz import Laeyerz

import os
from dotenv import load_dotenv
load_dotenv()


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


session_list = ly.load_session_list()
print("Session List : ",session_list)

#Create a new session
ly.create_session("Session Test 1")


curr_session = ly.load_session("Session Test 1")
print("Session : ",curr_session)

#Chatting with the session
response = curr_session.chat(

    {   
        "instructions":"Respond to the user's query based on the provided information.",
        "query":"What are the applications of RAG?"
    }
)
