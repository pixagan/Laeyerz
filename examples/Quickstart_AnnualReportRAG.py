# Created: Anil Variyar
# Quickstart Dataloader

from laeyerz.Laeyerz import Laeyerz
from laeyerz.LDocument import LDocument

import os
from dotenv import load_dotenv
load_dotenv()


#laeyers
config = {
    "appname": "Financial Report Example",
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

document = LDocument()
document.load_pdf("../datasets/AR_1.pdf")
chunks = document.into_chunks()

print(len(chunks))


document = {
    "type": "report",
    "title": "Financial Report Example",
    "chunks": chunks

}


#adding documents to Laeyerz
ly.add_document(document,'report')



session_list = ly.load_session_list()
print("Session List : ",session_list)

#Create a new session
ly.create_session("Fin Report Analysis")


curr_session = ly.load_session("Fin Report Analysis")
print("Session : ",curr_session)

#Chatting with the session
response = curr_session.chat(
    {   
        "instructions":"Respond to the user's query based on the provided information from the Financial Report",
        "query":"What is the revenue from OIL and GAS"
    }
)



print("Response : ",response["response"])