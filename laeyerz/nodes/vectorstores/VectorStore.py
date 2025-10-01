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
VectorStore module for vector store operations
in the Laeyerz framework.
"""

from laeyerz.memory.vectordbs.PineconeAdapter import PineconeAdapter

class VectorStore:

    def __init__(self, dbtype='Pinecone', dbParams=None, api_key=None):
        print("Initializing VectorDB")

        self.dbParams = dbParams

        if(dbtype == 'Pinecone'):
            self.db = PineconeAdapter(api_key)

            #check if index exists
            indexExists = self.db.check_index(self.dbParams["index_name"])

            if(not indexExists):
                self.db.create_index(self.dbParams["index_name"], self.dbParams["dimension"], self.dbParams["metric"])



        elif(dbtype == 'Chroma'):
            self.db = ChromaAdapter()
        else:
            raise ValueError("Invalid database type")


    #A collection is where embeddings for an app are stored ---

    def setup(self, config):
        print("Setting up VectorDB")

        self.db.setup(config)

    #--- create collection ----------------------------

    def createCollection(self, collection):
        print("Creating collection")

        self.db.createCollection(collection)


    def setCollection(self, collection):
        print("Setting collection")
        self.db.setCollection(collection)


    #--- delete collection ----------------------------


    def store(self, embeddings, metadata):
        print("Storing embeddings")

        self.db.insert_vectors(self.dbParams["index_name"], metadata, embeddings, namespace=self.dbParams["namespace"])



    def search(self, query_embedding, meta={}):

        print("Searching for embeddings : ",  query_embedding)
        
        search_results = self.db.search(self.dbParams["index_name"], query_embedding, k_nearest=3, namespace=self.dbParams["namespace"])

        return search_results


        

#----------------------------------------------------------------------


def main():

    vecdb = VectorDB()
 




#----------------------------------------------------------------------

if __name__ == "__main__":
    main()


#----------------------------------------------------------------------
