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

class Responder(Node):

    def __init__(self, name, config):
        super().__init__(name, {})

        self.name = name
      

        self.llm = config.get('llm')


    def setup(self):
        self.llm_instructions = """Given the task, the state of the task completion and the steps taken to complete the task,
        you now need to create the response to be returned to the user. The response should have two parts, 1) the parameters requested by the user which you need to extract from the state, this is the response to the user
        and 2) a summary of the steps taken to complete the task, show this as keypoints, each point a minimal summary of the step taken.
        Respond in the following json format:
        {
            "response": {
                "parameter_name": "parameter_value",
                "parameter_name": "parameter_value",
                ...
            } , // the response to the user
            "keypoints": [
                "Summary of the step taken",
                "Summary of the step taken",
                ...
            ] // a keypoint summary of the task completed
        }
        """


    def respond(self, task, state, completion_status):

        messages = [
            {
                "role": "system",
                "content": self.llm_instructions
            },
            {
                "role": "user",
                "content": f"Task: {task}"
            },
            {
                "role": "user",
                "content": f"Completion Status: {completion_status}"
            },
            {
                "role": "user",
                "content": f"State: {state}"
            },
        ]

        response = self.llm.call_llm(messages)

        content = response["message"].content

        content = json.loads(content)

        user_response = content["response"]
        task_keypoints = content["keypoints"]

        return user_response, task_keypoints