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


class Loop(Node):

    def __init__(self, node_name, config={}):
        super().__init__(node_name, config)
        self.nIters = 0
        self.flow  = {}


    def add_flow(self, flow):
        self.flow = flow


    def run(self, input_data):
        nIters = len(input_data)

        for flow in nIters:
            self.flow.run(input_data[iter])




    