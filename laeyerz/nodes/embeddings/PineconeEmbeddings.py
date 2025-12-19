# Copyright 2025 Pixagan Technologies
#
# Licensed under the Apache License, Version 2.0 (the "License");
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
PineconeEmbeddings module for Pinecone vector embeddings
in the Laeyerz framework.
"""

#import os
from laeyerz.flow.Node import Node
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec

#PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')

class PineconeEmbeddings(Node):
    
    def __init__(self, node_name, config={}):
        self.pc = Pinecone(api_key=config.get('api_key'))


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
