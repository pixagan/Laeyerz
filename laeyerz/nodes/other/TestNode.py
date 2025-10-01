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
TestNode module for testing and debugging
in the Laeyerz framework.
"""

class TestNode(Node):

    def __init__(self, node_name, params={}):
        super().__init__(node_type='Test', node_subtype='Test', node_name=node_name, description='Dummy Node to test Flows')
        self.function = self.test_function
        self.add_action(action_name="test_function", function=self.test_function, inputs=["text"], parameters=["model"], outputs=["output"])

    def setup(self):
        print(f"Setting up node {self.name}")

    def test_function(self, inputs):
        print(f"Test function {inputs}")
        text = inputs.get('text', '')
        response = text + " Hello from Test Node "
        return {"output": response}




def test_function(inputs):
    """Test Function"""
    # Extract inputs - you can customize this based on your needs
    text = inputs.get('text', '')
    
    
    # Placeholder for OpenAI API call
    # In a real implementation, you would call the OpenAI API here
    response = text + " Hello from Test Node "
    
    return {"output": response}


def create_test_node(node_name):
    """Factory function to create and return an TestNode"""
    # Create the OpenAINode with proper initialization
    TestNode = Node(
        node_type='Test',
        node_subtype='Test',
        node_name=node_name,
        description='Dummy Node to test Flows'
    )

    # Set the function and configure inputs/outputs
    TestNode.action = 'Test Node'
    TestNode.set_function(test_function)
    TestNode.inputs = ['text']  # Expected input parameters
    TestNode.outputs = ['output']  # Expected output parameters
    
    return TestNode


# # Create a default instance
# TestNode = create_test_node()


# Return the configured node
if __name__ == "__main__":
    # For testing the node
    from laeyerzflow.flow.AppState import AppState
    
    app_state = AppState()
    app_state.update('text', 'Hello from OpenAI!')
    app_state.update('model', 'gpt-4')
    
    # result, next_node = TestNode.run(app_state)
    # print(f"Result: {result}")
    # print(f"Next node: {next_node}")






