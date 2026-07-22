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

import simplejson as json

from laeyerz.flow.Node import Node
from llmbox.LLMNode import LLMNode

class Planner(Node):

    def __init__(self, name, config):
        super().__init__(name)
        self.name = name
      

        self.llm = config.get('llm')

    def plan_task(self, task, tools):
        
        planner_prompt = """
        You are a task planner. 
        You will be given the task description and the tools available to you.
        You need to create a plan for the agent to complete the task. The plan should be a sequence of steps.
        Each step is a single tool call. The sequence of steps should result in the task being completed.
        
        Respond ONLY with the plan in the following JSON format. Do not include any other text or comments:
        {
            "steps": [
                {
                    "step": 1,
                    "description": "Step 1 description", 
                    "tool": "tool_name",
                },
                {
                    "step": 2,
                    "description": "Step 2 description", 
                    "tool": "tool_name"
                }
                ...
            ]
        }
        """

        messages = [
            {
                "role": "system",
                "content": str(planner_prompt)
            },
            {
                "role": "user",
                "content": f"Task description: "+ str(task)
            }
        ]

        response = self.llm.call_llm(messages)

        plan = response["message"].content

        print("Plan: ", plan)

        plan = json.loads(plan)
        
        return plan

