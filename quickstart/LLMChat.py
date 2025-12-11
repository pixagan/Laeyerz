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

#load .env
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


from laeyerz.nodes.llm.OpenAILLMNode import OpenAILLMNode as LLM


#create LLM node
llm = LLM("Model")


#-------- Configure the Inputs to the LLM -----------
#pick the llm model
model = "gpt-5-mini"
tools = []

instructions = "You are a helpful assistant that can summarize the given text"
query = """Artificial intelligence (AI) refers to the ability of computer systems to perform tasks that traditionally require human intelligence. These tasks include learning from experience, reasoning through problems, recognizing patterns, understanding language, perceiving the environment, and making decisions. At its core, AI aims to create machines that can mimic or augment human cognitive abilities in a wide range of situations.

AI is a major field within computer science that develops theories, techniques, and software enabling machines to analyze information, adapt to new inputs, and take actions that help them achieve defined objectives. This involves multiple subfields, such as machine learning—which allows systems to improve performance through data—natural language processing, computer vision, robotics, and expert systems. Together, these technologies enable computers to make sense of complex environments and act intelligently within them.

Modern AI systems work by processing large amounts of data, identifying meaningful patterns, and learning rules or behaviors that help them solve specific problems. They can operate autonomously or as tools that enhance human decision-making. The ultimate goal of AI research is to build systems that are reliable, flexible, and capable of working efficiently in real-world scenarios, thereby increasing productivity, improving user experiences, and supporting better decisions across industries."""


#chat models require a set of inputs
messages = [
    {"role": "developer", "content": instructions},
    {"role": "developer", "content": "Tools: " + str(tools)},
    {"role": "user", "content": "query: " + query}
]

#set up an input dictionary for the llm
inputs  = {
    "model": model,
    "tools": [],
    "messages": messages,
}


#--------- Process the LLM Output -----------

#call the llm
output = llm.call_llm(messages, model, tools )

#output = llm.run('call_llm', inputs)

#extract the llm output
output_text = output['message'].content
#postprocess the llm output

print("Summary: ", output_text)

