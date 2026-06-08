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

from laeyerz.flow.Node import Node


class Loop(Node):

    def __init__(self, node_name, config={}):
        super().__init__(node_name, config)
        self.nIters = 0
        self.flow  = {}
        self.node_action = None
        self.run_loop = None

        self.add_actions()


    def set_flow(self, flow, type="flow", node_action=None):
        self.flow = flow
        self.type = type

        if type == "flow":
            self.run_loop = self.run_flow_loop
        elif type == "node":
            self.run_loop = self.run_node_loop
            self.node_action = node_action


    def run_node_loop(self, input_data=[], nIters=1):
        response = []

        nIters = len(input_data)

        print("nIters: ", nIters)

        for i in range(nIters):
            output = self.flow.run(self.node_action, input_data[i])
            response.append(output)
        return response


    def run_flow_loop(self, input_data=[], nIters=1):

        response = []

        nIters = len(input_data)

        print("nIters: ", nIters)

        for i in range(nIters):
           
            output = self.flow.run(input_data[i])
            response.append(output)

        return response


    def add_actions(self):

        loop_inputs = [
            {
                "name":"input_data",
                "type":"list",
                "description":"The list of input data to iterate over",
                "inputType":"input",
                "source":"",
            },
            {
                "name":"nIters",
                "type":"int",
                "description":"The number of iterations to return",
                "inputType":"input",
                "source":"",
            }
        ]
        loop_outputs = [
            {
                "name":"results",
                "type":"list",
                "description":"A list of outputs from the loop",
            }
        ]
        self.add_action(action_name="run_loop", function=self.run_loop, parameters=[], inputs=loop_inputs, outputs=loop_outputs, isDefault=True, description="Run the loop")






    