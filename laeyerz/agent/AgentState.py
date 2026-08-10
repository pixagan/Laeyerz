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

from laeyerz.flow.Steps import Steps
from laeyerz.flow.Node import Node

class AgentState(Node):

    def __init__(self, name, config):
        super().__init__(name)

        self.name = name
        self.config = config
        self.state = {}
        self.steps = Steps()
        self.task = None
        self.plan = None


    def add_step(self, step):
        self.steps.add_step(step)

    def get_steps(self):
        return self.steps.get_steps()


    def get_state(self):
        state = []
        for step in self.steps.get_steps():
            state.append({
                "step": step["step"],
                "type": step["type"],
                "name": step["name"],
                "content": step["content"],
            })
        return state


    def set_state(self, state):
        self.config["state"] = state


    def set_task(self, task):
        self.task = task

    def update_plan(self, plan):
        self.plan = plan