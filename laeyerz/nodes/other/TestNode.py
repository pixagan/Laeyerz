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


# Return the configured node
if __name__ == "__main__":
   





