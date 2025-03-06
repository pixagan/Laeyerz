# Created: Anil Variyar
# FAISS Adapter

import faiss
from sklearn.preprocessing import normalize
import numpy as np

class FaissIndex:

    def __init__(self,vector_dim):
        print("Faiss Indexing")

        self.nlist = 1 #100
        #self.num_vectors = num_vectors
        self.vector_dim  = vector_dim
        self.index = None


    def generate(self, vectors):

        num_vectors = len(vectors)
        vector_dim = self.vector_dim
        nlist      = self.nlist

        quantizer = faiss.IndexFlatL2(vector_dim) 
        index_ivf = faiss.IndexIVFFlat(quantizer, vector_dim, nlist, faiss.METRIC_L2)

        index_ivf.train(vectors)

        index_ivf.add(vectors)

        self.index = index_ivf


    def search(self, query_vector, k=5):

        distances, indices = self.index.search(query_vector, k)

        return distances, indices


    def export(self, filename):

        faiss.write_index(self.index, "vector_index.faiss")



    def load(self, filename):

        self.index = faiss.read_index("vector_index.faiss")




def main():

    

    # Example: Create random vectors
    num_vectors = 1000
    vector_dim  = 128

    vectors = np.random.rand(num_vectors, vector_dim).astype('float32')
    vectors = normalize(vectors, axis=1)


    fi = FaissIndex(vector_dim)

    fi.generate(vectors)


    query_vector = np.random.rand(1, vector_dim).astype('float32')
    query_vector = normalize(query_vector, axis=1)

    
    distances, indices = fi.search(query_vector)

    print(distances, indices)






#----------------------------------------------------------------------

if __name__ == "__main__":
    main()


#-------------------