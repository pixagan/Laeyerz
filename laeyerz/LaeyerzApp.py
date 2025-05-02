# Created: Anil Variyar
# Laeyerz App

## Deployable as a web application backend, extend this to make your application

import os

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

from dotenv import load_dotenv
load_dotenv()


from laeyerz.Laeyerz import Laeyerz
from laeyerz.LDocument import LDocument
from laeyerz.flow.AppBuilder import AppBuilder



# Initialize FastAPI app
app = FastAPI(
    title="Laeyerz API",
    description="Backend API for Laeyerz Application",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3547"],  # Add your React app's URL here
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)




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



# Example Pydantic model for data validation
class Conversation(BaseModel):
    title: str

class Chat(BaseModel):
    instructions: str
    query: str

class NodeInput(BaseModel):
    id: str
    type: str
    model: str
    inputs: dict



def serialize_response(item):
    """Convert response item to JSON-serializable format"""
    if isinstance(item, dict):
        return {
            key: str(value) if isinstance(value, ObjectId)
            else serialize_response(value)
            for key, value in item.items()
        }
    elif isinstance(item, list):
        return [serialize_response(i) for i in item]
    return item




class LaeyerzApp:

    def __init__(self):
        print("Initializing Laeyerz App Backend")

        self.api =  FastAPI(
                                title="Laeyerz API",
                                description="Backend API for Laeyerz Application",
                                version="1.0.0"
                            )

        self.api.add_middleware(
                                    CORSMiddleware,
                                    allow_origins=["http://localhost:3547"],  # Add your React app's URL here
                                    allow_credentials=True,
                                    allow_methods=["*"],  # Allows all methods
                                    allow_headers=["*"],  # Allows all headers
                                )



        self.setup_routes()


        self.app = AppBuilder()



    def setup_routes(self):


        #----------Sessions -----------
        # Basic CRUD routes
        @self.api.get("/")
        async def root():
            return {"message": "Welcome to Laeyerz API"}



        @self.api.get("/api/conversations")
        async def get_conversations():

            # Add your database logic here
            sessions = ly.load_session_list()

            # Convert ObjectId to string in the sessions list
            formatted_sessions = []
            for session in sessions:
                formatted_session = {
                    **session,
                    '_id': str(session['_id'])  # Convert ObjectId to string
                }
                formatted_sessions.append(formatted_session)

            print("Sessions : ",formatted_sessions)

            return {"sessions": formatted_sessions}



        @self.api.post("/api/conversations")
        async def create_conversation(item: Conversation):

            try:
                session = ly.create_session(item.title)
                if isinstance(session, dict) and '_id' in session:
                    session['_id'] = str(session['_id'])
                return session
            except Exception as e:
                print("Error:", str(e))  # Add this line for debugging
                raise HTTPException(status_code=500, detail=str(e))




        @self.api.get("/api/conversations/{conversation_id}")
        async def get_chats(conversation_id: str):
            # Add your database logic here

            print("Conversation ID : ", conversation_id)
            session = ly.load_session_by_id(conversation_id)
            chats = session.load_history()


            currSession = {
                "conversation_id": session.session_id,
                "title": session.title
            }

            # Convert ObjectId to string in the sessions list
            formatted_chats = []
            for chat in chats:
                formatted_chat = {
                    **chat,
                    '_id': str(chat['_id'])  # Convert ObjectId to string
                }
                formatted_chats.append(formatted_chat)

            return {"conversation": currSession, "chats": formatted_chats}





        @self.api.post("/api/conversations/{conversation_id}")
        async def chat(conversation_id: str, item: Chat):
            # Add your database logic here

            session = ly.load_session_by_id(conversation_id)
            response_item = session.chat(
                {
                    "instructions": item.instructions,
                    "query": item.query
                }
            )

            # Convert _id to string if it exists in the response
            if isinstance(response_item, dict) and '_id' in response_item:
                response_item['_id'] = str(response_item['_id'])
                
            return {"response": response_item}





        #-----------Flow -----------

        @self.api.post("/api/flow/node")
        async def add_node(conversation_id: str, item: NodeInput):
            # Add your database logic here

            self.app.add_node(item.id, item.type, item.model, item.inputs)

            response_item = {
                "status": "success",    
                "message": "Node added successfully"
            }
            return {"response": response_item}



        @self.api.post("/api/flow/edge")
        async def add_node(conversation_id: str, item: NodeInput):
            # Add your database logic here

            self.app.add_edge(item.id, item.type, item.model, item.inputs)

            response_item = {
                "status": "success",    
                "message": "Node added successfully"
            }
            return {"response": response_item}




#------------------------------



def main():
    # Run the FastAPI application
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()

