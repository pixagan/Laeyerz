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
SentenceTransformerAdapter module for sentence transformer embeddings
in the Laeyerz framework.
"""

from sentence_transformers import SentenceTransformer


class SentenceTransformerAdapter(Node):

    def __init__(self, model_name='paraphrase-MiniLM-L6-v2'):
        print("Initializing Sentence Transformer")
        self.model = SentenceTransformer(model_name)


    def encode(self, sentences):
        print("")

        embeddings_list = self.model.encode(sentences)

        return embeddings_list


def main():
    print("Starting Sentence Transformer Adapter")
    sentence_transformer_adapter = SentenceTransformerAdapter()
    sentence_transformer_adapter.encode(["Hello, how are you?"])
    print("Sentence Transformer Adapter started")

if __name__ == "__main__":
    main()