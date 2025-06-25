# Created: Anil Variyar
# FAISS Adapter

import faiss
from sklearn.preprocessing import normalize
import numpy as np
import uuid

class FaissAdapter:

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