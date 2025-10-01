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
EmbeddingModel module for text embeddings
in the Laeyerz framework.
"""

from laeyerz.flow.Node import Node
from laeyerz.embeddings.SentenceTransformerAdapter import SentenceTransformerAdapter
from laeyerz.embeddings.OpenAIEmbeddings import OpenAIEmbeddings
from laeyerz.embeddings.PineconeEmbeddings import PineconeEmbeddings

# Embeddings Models
# HuggingFace, Models : paraphrase-MiniLM-L6-v2
# OpenAI
# Pinecone


def get_embedding_model_dimensions(model_name):

    if(model_name == 'paraphrase-MiniLM-L6-v2'):
        return 384
    elif(model_name == 'text-embedding-3-small'):
        return 1536
    elif(model_name == 'text-embedding-3-large'):
        return 3072
    else:
        raise ValueError("Invalid vendor")



class EmbeddingModel(Node):

    def __init__(self, vendor='HuggingFace',model_name='paraphrase-MiniLM-L6-v2'):
        print("Initializing Embedding Model")

        self.model      = None
        self.vector_dim = 0

        if(vendor == 'HuggingFace'):
            self.model = SentenceTransformerAdapter(model_name)
            self.vector_dim = get_embedding_model_dimensions(model_name)
        elif(vendor == 'OpenAI'):
            self.model = OpenAIEmbeddings(model_name)
            self.vector_dim = get_embedding_model_dimensions(model_name)
        elif(vendor == 'Pinecone'):
            self.model = PineconeEmbeddings(model_name)
            self.vector_dim = get_embedding_model_dimensions(model_name)
        else:
            raise ValueError("Invalid vendor")

        

    def encode(self, sentences):
        print("")

        embeddings_list = self.model.encode(sentences)

        return embeddings_list

