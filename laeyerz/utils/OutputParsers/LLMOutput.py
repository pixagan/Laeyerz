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
LLMOutput module for LLM output parsing
in the Laeyerz framework.
"""


class LLMOutput(Node):

    def __init__(self, output):
        super().__init__(node_name="LLMOutput", description="LLM Output")
        self.metadata = {
            "node_type": "LLM",
            "node_subtype": "Output",
        }
        self.view = {
            "view_type": "LLM",
            "view_subtype": "Output",
        }
        self.output = output


    def parse(self, message):

        parsed_output = {
            "output": message,
        }
        return parsed_output


    def to_markdown(self, output):
        return f"## LLM Output\n\n{output}"
        

    def to_json(self, output):  
        return json.dumps(output)


llm_output = LLMOutput("Hello, how are you?")
llm_output.parse()