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

from laeyerz.nodes.Node import Node


class LLMOutputParser(Node):

    def __init__(self, node_name, config={}):
        super().__init__(node_name, config)


    def extract_open_ai_json(self, llm_out, format, values,):

        content = llm_out.get("content")



        print("Extracting OpenAI JSON from text")


        
    def add_actions(self):
        self.add_action(action_name="extract_open_ai_json", function=self.extract_open_ai_json, inputs=["text"], outputs=["text"])