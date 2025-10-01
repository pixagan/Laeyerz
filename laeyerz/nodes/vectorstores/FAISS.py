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
FAISS module for FAISS vector store operations
in the Laeyerz framework.
"""
# FAISS Adapter

import faiss
from sklearn.preprocessing import normalize
import numpy as np
import uuid

class FaissAdapter(Node):

    def __init__(self, vector_dim, alog="flat"):
        print("Faiss Indexing")

        
        self.vector_dim  = vector_dim
        self.index       = None

        self.index = faiss.IndexFlatL2(vector_dim)
        self.metadata = []



    def store(self, vectors, metadata):

        if(len(metadata) != len(vectors)):
            raise ValueError("Metadata and vectors must be of the same length") 

        # for md in metadata:
        #     md['id'] = str(uuid.uuid4())
            
        self.index.add(vectors)
        self.metadata.extend(metadata)


    def search(self, query_vector, k=3):

        distances, indices = self.index.search(query_vector, k)

        print("saved metadata : ",indices, distances)

        search_out = []
        for i in range(len(indices[0])):
            index = indices[0][i]
            search_out.append({
                "id":str(self.metadata[int(index)]["id"]),
                "metadata":self.metadata[int(index)]["metadata"],
                "score":str(distances[0][int(i)])
            })

        
        # search_out = [{
        #     "id":str(self.metadata[int(i)]["id"]),
        #     "metadata":self.metadata[int(i)]["metadata"],
        #     "score":str(distances[0][int(i)])
        #     } for i in indices[0]]
            

        return search_out


    def clear(self):
        self.index = None
        self.metadata = []


    def export(self, filename):

        faiss.write_index(self.index, "vector_index.faiss")



    def load(self, filename):

        self.index = faiss.read_index("vector_index.faiss")




def main():

    

    # Example: Create random vectors
    num_vectors = 100
    vector_dim  = 128

    vectors = np.random.rand(num_vectors, vector_dim).astype('float32')
    vectors = normalize(vectors, axis=1)


    vector_store = FaissStore(vector_dim)

    vector_store.add(vectors)

    distances, indices = vector_store.search(vectors[1].reshape(1,-1),3)

    print(distances, indices)


#----------------------------------------------------------------------

if __name__ == "__main__":
    main()


#-------------------


def faiss_function(inputs):
    """Faiss function that processes inputs and returns output"""
    # Extract inputs - you can customize this based on your needs
    chunks = inputs.get('text', '')
    embedding_model = inputs.get('model', 'gpt-3.5-turbo')
    
    # Placeholder for OpenAI API call
    # In a real implementation, you would call the OpenAI API here
    response = f"Faiss processed: {text} using {model}"
    
    return {"output": response}


def create_faiss_node(node_name):
    """Factory function to create and return an FaissNode"""
    # Create the FaissNode with proper initialization
    FaissNode = Node(
        node_type='Faiss',
        node_subtype='Vector Store',
        node_name=node_name,
        description='Node for FAISS API interactions'
    )

    # Set the function and configure inputs/outputs
    FaissNode.action = 'Faiss Vector Store call'
    FaissNode.set_function(faiss_function)
    FaissNode.inputs = ['text', 'model']  # Expected input parameters
    FaissNode.outputs = ['output']  # Expected output parameters
    
    return FaissNode


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






