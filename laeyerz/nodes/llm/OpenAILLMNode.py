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
OpenAILLMNode module for OpenAI LLM integration
in the Laeyerz framework.
"""
from openai import OpenAI
from dotenv import load_dotenv
import os
import json
from laeyerz.flow.Node import Node

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

class OpenAILLMNode(Node):

    def __init__(self, node_name, config={}):
        super().__init__(node_name=node_name, description='OpenAI LLM Node')
        self.metadata = {
            "node_type": "OpenAI",
            "node_subtype": "LLM",
        }
        self.view = {
            "view_type": "OpenAI",
            "view_subtype": "LLM",
        }
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.add_action(action_name="call_llm", function=self.call_llm, inputs=["messages", "model"], parameters=["model"], outputs=["outputs"], isDefault=True)

    

    def setup(self):
        print(f"Setting up node {self.name}")

    def call_llm(self, inputs):
        messages = inputs.get('messages')
        model    = inputs.get('model')
        tools    = inputs.get('tools')
        output_format = inputs.get('output_format')

        print("Messages : ", messages)
        print("Model : ", model)
        print("Tools : ", tools)

        response = self.client.chat.completions.create(
                model=model,
                messages = messages,
                tools = [],
                tool_choice = "auto"
        )

        message       = response.choices[0].message
        finish_reason = response.choices[0].finish_reason
        tool_calls    = response.choices[0].message.tool_calls


        outputs = self.response_parser(response)
        return outputs



    def response_parser(self, response):

        #response = 

        parsed_response = {
            "completion_id": response.id,
            "model": response.model,
            "message": response.choices[0].message,
            "content": response.choices[0].message.content,
            "created": response.created,
            "finish_reason": response.choices[0].finish_reason,
            #"usage": response.usage,
            "tokens_used": response.usage.total_tokens,
            "tokens_prompt": response.usage.prompt_tokens,
            "tokens_completion": response.usage.completion_tokens,
            "service_tier": response.service_tier,
            "tool_calls": [],
        }


        tool_calls = response.choices[0].message.tool_calls

        tool_call_extracted = []

        if tool_calls:
            for tc in tool_calls:
                function_name = tc.name
                arguments = json.loads(tc.function.arguments)
                tool_call_extracted.append({
                    "function_name": function_name,
                    "arguments": arguments
                })

        parsed_response["tool_calls"] = tool_call_extracted
        

        return parsed_response





# Return the configured node
if __name__ == "__main__":
    # For testing the node

    llm_node = OpenAILLMNode("LLM", "gpt-4o-mini")

    llm_node.call_llm({"messages": [{"role": "user", "content": "Hello, how are you?"}], "model": "gpt-4o-mini"})
  
    
    # result, next_node = OpenAINode.run(app_state)
    # print(f"Result: {result}")
    # print(f"Next node: {next_node}")






