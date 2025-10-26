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
TextInput module for text input operations
in the Laeyerz framework.
"""
from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

class TextInputNode(Node):

    def __init__(self, node_name, params={}):
        super().__init__(node_type='TextInput', node_name=node_name,  node_subtype='Input', description='Text Input Node')
        self.add_action(action_name="input_text", function=self.input_text, inputs=["input"], parameters=["None"], outputs=["text_input"], isDefault=True)

    def setup(self):
        print(f"Setting up node {self.name}")

    def input_text(self, inputs):
        text_input = inputs.get('input')

        print("Text Input : ", text_input)

        return text_input






