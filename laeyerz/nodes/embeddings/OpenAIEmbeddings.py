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
OpenAIEmbeddings module for OpenAI text embeddings
in the Laeyerz framework.
"""

#import os
from openai import OpenAI
from laeyerz.flow.Node import Node

#from dotenv import load_dotenv
#load_dotenv()

#OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


default_messages = [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "usecr", "content": "Write a haiku about programming."}
                ]


class OpenAIEmbeddings(Node):

    def __init__(self, node_name, config={}):
        print("Initializing OpenAI adapter")
        super().__init__(node_name, config)

        self.model  = config.get('model_name', 'gpt-4o-mini')
        self.client =  OpenAI(api_key=config.get('api_key'))


    def encode(self, text):
        print("Generate embeddings")

        response = self.client.embeddings.create(input=text)

        return response.data[0].embedding




# ------------------------------------------------------------------

def main():

    chat = OpenAIAdapter()
    output = chat.run()
    print(output)

    


#----------------------------------------------------------------------

if __name__ == "__main__":
    main()


#----------------------------------------------------------------------

        



