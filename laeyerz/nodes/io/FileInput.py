# Copyright (c) 2025 Pixagan Technologies
#
# Licensed under the BSD License. See LICENSE file in the project root for
# full license information.

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






