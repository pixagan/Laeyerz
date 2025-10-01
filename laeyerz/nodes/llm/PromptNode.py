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
PromptNode module for prompt management
in the Laeyerz framework.
"""

class PromptNode(Node):

    def __init__(self, node_name, params={}):
        super().__init__(node_type='Prompt', node_name=node_name, node_subtype='LLM', description='Prompt Node')
        self.actions = []
        self.items = []
        self.add_action(action_name="generate_prompt", function=self.generate_prompt, inputs=["model"], parameters=["model"], outputs=["prompt"], isDefault=True)


    def setup(self):
        print(f"Setting up node {self.name}")


    def add_item(self, item):
        self.items.append(item)


    def get_items(self):
        return self.items


    def generate_prompt(self, inputs):


        for key, value in inputs.items():
            if key == "model":
                model = value
            else:
                self.add_item(value)




        prompt = ""
        for item in self.items:
            prompt += item + "\n"
        return prompt


