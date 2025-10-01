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
TestNode module for testing Node functionality
in the Laeyerz framework.
"""

from laeyerz.flow.Node import Node
from laeyerz.flow.AppState import AppState

def model0(input0:str)->(str):
    
    print("Model 0 :", input0)

    output = "output0"
    output1 = "output1"

    return output, output1


node = Node("TestNode")

app_state = AppState()
app_state.add_section("TestNode")

app_state.update("Inputs", "input0", "Hello")

print(app_state.get_all())

node.inputs  = {"Inputs:input0":"input0"}
node.outputs = {"output0":"TestNode:output0"}
node.set_function(model0)


#node.function("Hello")

node.run(app_state)


print(app_state.get_all())