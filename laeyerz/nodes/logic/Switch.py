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
SwitchNode module for conditional logic operations
in the Laeyerz framework.
"""

from laeyerz.flow.Node import Node

class SwitchNode(Node):

    def __init__(self, node_id, node_name, node_description):
        super().__init__(node_id, node_name, node_description)

    def setup(self):
        self.add_action(action_name="switch", function=self.switch, inputs=["input"], parameters=["condition"], outputs=["output"])

    def switch(self, input, condition):
        return input