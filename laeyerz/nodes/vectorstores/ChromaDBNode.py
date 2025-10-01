# Copyright 2025 Pixagan Technologies
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
ChromaDBNode module for ChromaDB vector store operations
in the Laeyerz framework.
"""
from laeyerz.flow.Node import Action

class ChromaDBNode(Node):

    def __init__(self, node_name, params={}):
        super().__init__(node_type='Chroma', node_name=node_name, node_subtype='Vector Store', description='ChromaDB Node')

        self.client     = None
        self.collection = None

        
        self.add_action(action_name="add_documents", function=self.add_documents, inputs=["documents"], parameters=["model"], outputs=["output"], isDefault=True)
        self.add_action(action_name="query_documents", function=self.query_documents, inputs=["query"], parameters=["model"], outputs=["output"])

        self.params = {
            "db_path": "default",
            "collection_name": "default",
            "embedding_model": "default",
            "similarity_metric": "default",
            "similarity_threshold": 0.5,
            "similarity_top_k": 5,
            "similarity_filter": "default",
        }


    def setup(self):
        print(f"Setting up node {self.name}")


    def connect(self, connection_type, url, api_key):
        if connection_type == "chroma":
            self.client = chroma.Client(url=url, api_key=api_key)
        elif connection_type == "faiss":
            self.client = faiss.Index(url)
        else:
            raise ValueError(f"Invalid connection type: {connection_type}")

    
    def query_documents(self, collection_name, query):
        collection = self.get_collection(collection_name)
        results = collection.query(
            query_texts=[query], # Chroma will embed this for you
            n_results=5 # how many results to return
        )
        return results

    def get_collections(self):
        return self.client.list_collections()


    def create_collection(self, name):
        collection = self.client.create_collection(name=name)
        return collection


    def get_collection(self, collection_name):
        collection = self.client.get_or_create_collection(name="my_collection")
        return collection


    def add_documents(self, collection_name, documents, metadata=[]):
        
        collection = self.get_collection(collection_name)
        
        ids = [str(uuid.uuid4()) for _ in documents]
        
        collection.upsert(
            ids=ids,
            documents=documents,
            metadatas=metadata
        )

        return ids



    def delete_collection(self, collection_name, ids=[]):
        self.client.delete_collection(name=collection_name)


    def delete_documents(self, collection_name, ids):
        if len(ids) > 0:
            collection = self.get_collection(collection_name)
            collection.delete(ids=ids)



    def update_collection(self, collection_name, ids, documents):
        collection = self.get_collection(collection_name)
        collection.upsert(ids=ids, documents=documents)





def chroma_function(inputs):
    """Chroma function that processes inputs and returns output"""
    # Extract inputs - you can customize this based on your needs
    chunks = inputs.get('text', '')
    embedding_model = inputs.get('model', 'gpt-3.5-turbo')
    
    # Placeholder for OpenAI API call
    # In a real implementation, you would call the OpenAI API here
    response = f"Chroma processed: {text} using {model}"
    
    return {"output": response}


def create_chroma_node(node_name):
    """Factory function to create and return an ChromaNode"""
    # Create the ChromaNode with proper initialization
    ChromaNode = Node(
        node_type='Chroma',
        node_subtype='Vector Store',
        node_name=node_name,
        description='Node for Chroma API interactions'
    )

    # Set the function and configure inputs/outputs
    ChromaNode.action = 'Chroma Vector Store call'
    ChromaNode.set_function(chroma_function)
    ChromaNode.inputs = ['text', 'model']  # Expected input parameters
    ChromaNode.outputs = ['output']  # Expected output parameters
    
    return ChromaNode


# Create a default instance
#FaissNode = create_faiss_node()


# Return the configured node
if __name__ == "__main__":
    # For testing the node
    from laeyerzflow.flow.AppState import AppState
    
    app_state = AppState()
    app_state.update('text', 'Hello from OpenAI!')
    app_state.update('model', 'gpt-4')
    
    # result, next_node = OpenAINode.run(app_state)
    # print(f"Result: {result}")
    # print(f"Next node: {next_node}")






