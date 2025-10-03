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
TestFlow module for testing Flow functionality
in the Laeyerz framework.
"""

from laeyerz.flow.Flow import Flow
from laeyerz.flow.Node import Node
from laeyerz.flow.AppState import AppState

## Create Functional Nodes
simple_flow = Flow("Flow 1")

simple_flow.state.update("Inputs", "input0", "Hello")

def model0(input0:str)->(str):

    print("Model 0 :", input0)

    output = input0+"_model0"

    return output

node1 = Node("Model0")
node1.inputs  = {"Inputs:input0":"input0"}
node1.outputs = {"output0":"Model0:output0"}
node1.set_function(model0)
simple_flow.add_node(node1)



def model1(input1:str)->(str):

    print("Model 1 :", input1)

    output = input1 + "_model1"

    return output

node2 = Node("Model1")
node2.inputs  = {"Model0:output0":"input1"}
node2.outputs = {"output1":"Model1:output1"}
node2.set_function(model1)
simple_flow.add_node(node2)


def model2(input2:str)->(str):
    

    print("Model 2 :", input2)

    output = input2 + "_model2"

    return output

node3 = Node("Model2")
node3.inputs  = {"Model1:output1":"input2"}
node3.outputs = {"output2":"Outputs:output2"}
node3.set_function(model2)
simple_flow.add_node(node3)






# Add edges to define your workflow
simple_flow.add_edge("START", "Model0")
simple_flow.add_edge("Model0", "Model1")
simple_flow.add_edge("Model1", "Model2")
simple_flow.add_edge("Model2", "END")

#finalize the flow - let flow make required pre computations, generate structures
simple_flow.finalize()

#run the flow
input_data = {
    "input0": "Hello, world!"
}
output = simple_flow.run(input_data)

print("Output : ", output)
print("History : ", simple_flow.steps)

#----------------------- Visualization -------------------------------

from laeyerz.ui.LaeyerzAPI import LaeyerzVizAPI

lflow = LaeyerzVizAPI()

lflow.set_flow(simple_flow)

lflow.run(host="0.0.0.0", port=6222)