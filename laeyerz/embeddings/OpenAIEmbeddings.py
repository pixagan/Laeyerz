# Created: Anil Variyar
# OpenAI Embeddings

import os
from openai import OpenAI

from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


default_messages = [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "usecr", "content": "Write a haiku about programming."}
                ]


class OpenAIEmbeddings:

    def __init__(self, model_name='gpt-4o-mini'):
        print("Initializing OpenAI adapter")

        self.model = model_name

        self.client =  OpenAI(api_key=OPENAI_API_KEY)


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

        



