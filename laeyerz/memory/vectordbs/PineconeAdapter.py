# Created: Anil Variyar
# Pinecone Adapter

import os
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec

PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')


class PineconeAdapter:
    
    def __init__(self, spec=None):
        self.pc   = Pinecone(api_key=PINECONE_API_KEY)
        self.spec = ServerlessSpec(cloud='aws', region='us-east-1')

    def setup(self, config):
        print("Setting up Pinecone")

       # self.create_index(config['name'], config['dimension'], config['metric'], config['spec'])


    def create_index(self, name, dimension=1024, metric="cosine", spec=None):
        print("Creating collection")

        self.create_index(name, dimension, metric, self.spec)

    

    def generate_embeddings(self, data, model="multilingual-e5-large"):
        #Generate Embeddings using deployed models

        embeddings = self.pc.inference.embed(
            model=model,
            inputs=[d['text'] for d in data],
            parameters={"input_type": "passage", "truncate": "END"}
        )

        return embeddings.data

    
    #Index -----

    def check_index(self, index_name):
        #check if index exists
        return self.pc.has_index(index_name)
    
    def create_index(self, index_name='default', dimension=1024, metric="cosine", spec=None):
        #Creating the index
        
        if self.spec is None:
            self.spec = ServerlessSpec(cloud='aws', region='us-east-1')

        if not self.pc.has_index(index_name):
            self.pc.create_index(
                name=index_name,
                dimension=dimension,
                metric=metric,
                spec=self.spec
            )

        while not self.pc.describe_index(index_name).status['ready']:
            time.sleep(1)



    def delete_index(self, index_name):
        #delete the index

        self.pc.delete_index(index_name)

    
    #-----Vectors
    

    def insert_vectors(self, index_name, data, embeddings, namespace="demo1-namespace"):
        #insert vectors

        index = self.pc.Index(index_name)

        records = [
            {
            "id": d['id'], 
             "values": e, 
             "metadata": {'text': d['text']}
            }
            for d, e in zip(data, embeddings)]

        index.upsert(vectors=records, namespace=namespace)
        

    def search(self, index_name, query_embedding, k_nearest=3, namespace="demo1-namespace"):
        #query
        
        index = self.pc.Index(index_name)
        
        results = index.query(
            namespace=namespace,
            vector=query_embedding,
            top_k=k_nearest,
            include_values=False,
            include_metadata=True
        )
        
        return results



    def modify_vectors(self, index_name, id, values, metadata, namespace="demo1-namespace"):
        #modify vectors
        

        index = self.pc.Index(index_name)

        index.update(
        	id=id, 
        	values=values, 
        	set_metadata=metadata,
        	namespace=namespace
        )

    
        
    def delete_vector(self, index_name, vector_ids, namespace='demo1-namespace'):
        #delete vectors
        
        index = self.pc.Index(index_name)
        index.delete(ids=vector_ids, namespace=namespace)
        



        

#----------------------------------------------------------------------




def main():

    pc = PineconeAdapter()
 

    text = [
       "At Swiggy, our mission is to elevate the quality of life for urban consumers by offering unparalleled convenience. Innovation has been an integral part of our DNA which encourages us to ideate, experiment and iterate constantly with the focus on identifying and addressing convenience needs of our users at the core of our innovation approach.",
       "Being among the first hyperlocal commerce platforms, Swiggy has successfully pioneered the industry in India, launching Food Delivery in 2014. Today, Swiggy offers its Food Delivery service in 653 cities across India serving ~13mn users1 through a wide network of 196k restaurant partners2. Our sharp focus on innovation coupled with strong execution yielded yet another milestone - we became one of the very few global food delivery platforms to achieve EBITDA profitability in less than 9 years since inception.",
       "We also pioneered Quick Commerce in India with the launch of Instamart in 2020, offering on-demand grocery and a growing array of household items delivered to our users in less than 10-15 minutes. We have successfully scaled our Quick Commerce offering to 27 cities delivering a wide array of ~17k SKUs through a dense network of 523 active dark stores."
        
    ]

    pc.create_index()

    pc.insert(insert_vectors)




#----------------------------------------------------------------------

if __name__ == "__main__":
    main()


#----------------------------------------------------------------------
