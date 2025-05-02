# Created: Anil Variyar
# OpenAI Adapter

import os
from openai import OpenAI

from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


default_messages = [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "usecr", "content": "Write a haiku about programming."}
                ]


class AnthropicAdapter:

    def __init__(self, model_name='gpt-4o-mini'):
        print("Initializing OpenAI adapter")

        self.model = model_name
        self.stream = False

        self.client =  OpenAI(api_key=OPENAI_API_KEY)


    def model_parameters(self, model_name):

        params = {
            "max_output_tokens": 1000,
            "previous_response_id": None,
            "temperature": 0.5,
            "top_p": 1,
            "truncation": True,
            "frequency_penalty": 0,
            "presence_penalty": 0,
            "stop": ["\n\n"],
            
        }


    def generate_prompt(self, instructions, query, memories):

        messages = []

        messages.append({"role": "system", "content": instructions})
        
        

        prompt = f"""
        {query}
        Information :{memories}
        """

        messages.append({"role": "user", "content": prompt})
        

        return messages


    def run(self, model_name, instructions, query, memories, params={}, tools = None):
        print("Run")

        messages = self.generate_prompt(instructions, query, memories)


        try:
            # Make a call to the OpenAI API
            response = self.client.chat.completions.create(
                model=model_name,
                messages=messages,
                tools=tools
            )
            #print("Response : ",response)

            parsed_response = self.response_parser(response)

            # Extract and return the response content
            return parsed_response #response.choices[0].message.content

        except Exception as e:
            return f"An error occurred: {e}"




    def response_parser(self, response):

        #response = 

        parsed_response = {
            "completion_id": response.id,
            "response": response.choices[0].message.content,
            "created": response.created,
            "model": response.model,
            #"usage": response.usage,
            "tokens_used": response.usage.total_tokens,
            "tokens_prompt": response.usage.prompt_tokens,
            "tokens_completion": response.usage.completion_tokens,
            "service_tier": response.service_tier,
        }

       
        return parsed_response

# ------------------------------------------------------------------

def main():

    chat = OpenAIAdapter()
    output = chat.run()
    print(output)

    


#----------------------------------------------------------------------

if __name__ == "__main__":
    main()


#----------------------------------------------------------------------

        



