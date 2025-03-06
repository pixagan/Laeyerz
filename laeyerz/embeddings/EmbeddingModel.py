# Created: Anil Variyar
# Embedding Model

from laeyerz.embeddings.SentenceTransformerAdapter import SentenceTransformerAdapter
from laeyerz.embeddings.OpenAIEmbeddings import OpenAIEmbeddings
from laeyerz.embeddings.PineconeEmbeddings import PineconeEmbeddings

# Embeddings Models
# HuggingFace, Models : paraphrase-MiniLM-L6-v2
# OpenAI
# Pinecone



class EmbeddingModel:

    def __init__(self, vendor='HuggingFace',model_name='paraphrase-MiniLM-L6-v2'):
        print("Initializing Embedding Model")

        self.model = None

        if(vendor == 'HuggingFace'):
            self.model = SentenceTransformerAdapter(model_name)
        elif(vendor == 'OpenAI'):
            self.model = OpenAIEmbeddings(model_name)
        elif(vendor == 'Pinecone'):
            self.model = PineconeEmbeddings(model_name)
        else:
            raise ValueError("Invalid vendor")

        

    def encode(self, sentences):
        print("")

        embeddings_list = self.model.encode(sentences)

        return embeddings_list