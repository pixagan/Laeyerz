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
FileInput module for file input operations
in the Laeyerz framework.
"""
from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

class FileInputNode(Node):

    def __init__(self, node_name, params={}):
        super().__init__(node_type='FileInput', node_name=node_name,  node_subtype='Input', description='File Input Node')
        self.add_action(action_name="load_file", function=self.load_file, inputs=["filename", "filetype"], parameters=["None"], outputs=["file_data"], isDefault=True)

    def setup(self):
        print(f"Setting up node {self.name}")

    def load_file(self, inputs):
        filename = inputs.get('filename')
        filetype = inputs.get('filetype')

        print("File Input : ", filename)

        file_data = {}

        return file_data






