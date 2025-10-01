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
ReActAgent module for ReAct agent implementation
in the Laeyerz framework.
"""



class ReActAgent:
    
    def __init__(self, llm_call_fn, tools: List, tool_lib: Dict[str, Any], max_iters: int = 10):
        self.llm_call  = llm_call_fn
        self.tools     = llm_tools
        self.tool_lib  = tool_lib
        self.max_iters = max_iters

        self.system_prompt = """ """


        self.messages = []

        self.token_count = []


    def llm_node(self):
        print("agent llm node")

        messages = self.messages
        
        finish_reason, message, tool_calls = self.llm_call(messages, tools=self.tools)

        llm_response = message
        
        self.messages.append(llm_response)

        return {
            "finish_reason":finish_reason,
            "message":message,
            "tool_calls":tool_calls
        }

        


    def tool_node(self, tool_calls):
        print("tool node")

        tool_responses = {}
        for call in tool_calls:
            function_name = call.name
            arguments = json.loads(call.function.arguments)
            response = self.tool_lib[function_name](**arguments)
            tool_responses[function_name] = response
                

        self.messages.append(tool_responses)

    
    def invoke(self, email, max_iters = 10):

        agent_response = {}

        self.messages.append()
        
        for iteration in range(0, self.max_iters):

            llm_response = self.llm_node()

            tool_calls = llm_response["tool_calls"]

            if(next == "tools"):
                self.tool_node(output.tool_calls)

            elif(next == "stop"):
                agent_response = output
                break

        return agent_response

    


