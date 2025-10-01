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
PreBuiltPicker module for selecting and creating pre-built nodes
in the Laeyerz framework.
"""


from laeyerzflow.flow.Node import Node
from laeyerzflow.prebuilt.LLM.OpenAILLMNode import OpenAILLMNode
from laeyerzflow.prebuilt.Other.TestNode import create_test_node, TestNode
from laeyerzflow.prebuilt.VectorStores.FAISS import create_faiss_node
from laeyerzflow.prebuilt.VectorStores.Pinecone import create_pinecone_node
from laeyerzflow.prebuilt.VectorStores.ChromaDBNode import ChromaDBNode
from laeyerzflow.prebuilt.DBs.Sqlite import create_sqlite_node
from laeyerzflow.prebuilt.LLM.PromptNode import PromptNode
from laeyerzflow.prebuilt.IO.FileInput import FileInputNode
from laeyerzflow.prebuilt.IO.TextInput import TextInputNode
from laeyerzflow.prebuilt.LLM.PromptNode import PromptNode


def get_prebuilt_node(node_type, node_name):

    if node_type == "Test_Node":
        newNode = TestNode(node_name)
        return newNode
        #return create_test_node(node_name)

    elif node_type == "Prompt":
        newNode = PromptNode(node_name)
        #return create_test_node(node_name)
        return newNode

    elif node_type == "OpenAI":
        newNode = OpenAILLMNode(node_name)
        return newNode
        #return create_openai_node(node_name)

    elif node_type == "Chroma":
        newNode = ChromaDBNode(node_name)
        return newNode

    elif node_type == "Faiss":
        return create_faiss_node(node_name)

    elif node_type == "Pinecone":
        return create_faiss_node(node_name)


        #return create_chroma_node(node_name)

    elif node_type == "Sqlite":
        return create_sqlite_node(node_name)


    elif node_type == "FileInput":
        newNode = FileInputNode(node_name)
        return newNode

    elif node_type == "TextInput":
        newNode = TextInputNode(node_name)
        return newNode
        

    elif node_type == "Custom":
        customNode = Node(node_type, node_name)
        customNode.action = "Custom"
        return customNode
    else:
        raise ValueError(f"Node type {node_type} not found")