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
OllamaNode module for Ollama LLM integration
in the Laeyerz framework.
"""

from laeyerz.flow.Node import Node
import os

class LLM_Ollama(Node):
    def __init__(self, node_name, config={}):
        super().__init__(node_name, config)
        self.add_action(action_name="call_llm", function=self.call_llm, inputs=["messages", "model"], parameters=["model"], outputs=["outputs"], isDefault=True)
