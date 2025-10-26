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
RAG module for Retrieval Augmented Generation example
in the Laeyerz framework.
"""
from laeyerz.nodes.LLM import OpenAILLMNode
from laeyerz.nodes.VectorStores import ChromaVectorStoreNode
from laeyerz.nodes.DataLoaders import PDLLoader
from laeyerz.nodes.DataProcessors import TextProcessor

#Flow 1

flow1 = Flow("Store")

#Pdf Input Node
pdf_input_node = PDLLoader("Pdf Input", "pdfs/sample.pdf")
pdf_input_node.input_map([("pdf_path", "INPUTS:pdf_path")])
flow1.add_node(pdf_input_node)


#Document Processor Node
document_processor_node = TextProcessor("Document Processor", "text/plain")
document_processor_node.input_map([("text", "pdf_input_node:text")])
flow1.add_node(document_processor_node)


#Vector STore Node
vector_store_node = ChromaVectorStoreNode("Vector Store", "chroma_db")
vector_store_node.set_action("store")
vector_store_node.input_map([("text", "document_processor_node:text")])
flow1.add_node(vector_store_node)



# Flow 2
flow1 = Flow("Retrieve")

#TextInput Node
text_input_node = TextInputNode("Text Input", "text/plain")
text_input_node.input_map([("text", "INPUTS:text")])
flow2.add_node(text_input_node)


#Vector Store Node
vector_store_node_r = ChromaVectorStoreNode("Vector Store", "chroma_db")
vector_store_node_r.input_map([("text", "text_input_node:text")])
flow2.add_node(vector_store_node_r)


#LLM Node
llm_node = OpenAILLMNode("LLM", "gpt-4o-mini")
llm_node.input_map([("text", "vector_store_node_r:text")])
flow2.add_node(llm_node)
