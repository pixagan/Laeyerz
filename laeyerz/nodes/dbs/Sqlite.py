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
Sqlite module for SQLite database operations
in the Laeyerz framework.
"""

from laeyerz.flow.Node import Node

class Sqlite(Node):

    def __init__(self, node_name, config={}):
        super().__init__()
        self.sqlite_function = self.sqlite_function
        self.inputs = ['text', 'model']
        self.outputs = ['output']

    def sqlite_function(self, inputs):
        """Sqlite function that processes inputs and returns output"""
        # Extract inputs - you can customize this based on your needs
    
        # In a real implementation, you would call the OpenAI API here
        response = f"Sqlite processed: {text} using {model}"
        
        return {"output": response}


    def create_sqlite_node(self, node_name):
        """Factory function to create and return an SqliteNode"""
        # Create the SqliteNode with proper initialization
        SqliteNode = Node(
            node_type='Sqlite',
            node_subtype='SQL DB',
            node_name=node_name,
            description='Node for Sqlite API interactions'
        )

        # Set the function and configure inputs/outputs
        SqliteNode.action = 'Sqlite LLM call'
        SqliteNode.set_function(sqlite_function)
        SqliteNode.inputs = ['text', 'model']  # Expected input parameters
        SqliteNode.outputs = ['output']  # Expected output parameters
        
        return SqliteNode


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






