# Created: Anil Variyar
# Pinecone Embeddings

import os

from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec

PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')


class PineconeEmbeddings:
    
    def __init__(self):
        self.pc = Pinecone(api_key=PINECONE_API_KEY)



    def encode(self, data):
        #Generate Embeddings using deployed models

        embeddings = self.pc.inference.embed(
            model="multilingual-e5-large",
            inputs=[d['text'] for d in data],
            parameters={"input_type": "passage", "truncate": "END"}
        )

        #return list of embeddings
        return embeddings.data

    



        

#----------------------------------------------------------------------




def main():

    pc = PineconeEmbeddings()
 


#----------------------------------------------------------------------

if __name__ == "__main__":
    main()


#----------------------------------------------------------------------
