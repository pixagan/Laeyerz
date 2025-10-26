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
OllamaNode module for Ollama LLM integration
in the Laeyerz framework.
"""

from laeyerz.flow.Node import Node
import os

class LLM_Ollama(Node):
    def __init__(self, node_name, config={}):
        super().__init__(node_name, config)
        self.add_action(action_name="call_llm", function=self.call_llm, inputs=["messages", "model"], parameters=["model"], outputs=["outputs"], isDefault=True)

def ollama_function(inputs):
    """OpenAI function that processes inputs and returns output"""
    # Extract inputs - you can customize this based on your needs
    text = inputs.get('text', '')
    model = inputs.get('model', 'gpt-3.5-turbo')
    
    # Placeholder for OpenAI API call
    # In a real implementation, you would call the OpenAI API here
    response = f"OpenAI processed: {text} using {model}"
    
    return {"output": response}


def create_ollama_node(node_name):
    """Factory function to create and return an OpenAINode"""
    # Create the OpenAINode with proper initialization
    OpenAINode = Node(
        node_type='OpenAI',
        node_subtype='LLM',
        node_name=node_name,
        description='Node for OpenAI API interactions'
    )

    # Set the function and configure inputs/outputs
    OpenAINode.action = 'OpenAI LLM call'
    OpenAINode.set_function(openai_function)
    OpenAINode.inputs = ['text', 'model']  # Expected input parameters
    OpenAINode.outputs = ['output']  # Expected output parameters
    
    return OpenAINode


# Create a default instance
#OpenAINode = create_openai_node()


# Return the configured node
if __name__ == "__main__":
    # For testing the node
    from laeyerzflow.flow.AppState import AppState
    
    app_state = AppState()
    app_state.update('text', 'Hello from OpenAI!')
    app_state.update('model', 'gpt-4')
    
    # result, next_node = OpenAINode.run(app_state)
    # print(f"Result: {result}")
    # print(f"Next node: {next_node}")






