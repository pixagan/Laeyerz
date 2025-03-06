# Created: Anil Variyar
# Sentence Transformer Adapter

from sentence_transformers import SentenceTransformer


class SentenceTransformerAdapter:

    def __init__(self, model_name='paraphrase-MiniLM-L6-v2'):
        print("Initializing Sentence Transformer")
        self.model = SentenceTransformer(model_name)


    def encode(self, sentences):
        print("")

        embeddings_list = self.model.encode(sentences)

        return embeddings_list