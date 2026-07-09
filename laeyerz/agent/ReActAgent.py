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

from datetime import datetime
import json

from laeyerz.flow.Node import Node
from laeyerz.utils.KeyManager import KeyManager
from laeyerz.flow.Steps import Steps
#from laeyerz.nodes.llm.OpenAINode import OpenAINode as LLM


class ReActAgent(Node):

   # def __init__(self, name, config, api_key_path, model, role, instructions, tools):
    def __init__(self, name, config):
        super().__init__(name)


        self.name = name
        api_key_path = config.get("api_key_path")
        role         =  config.get("role")
        instructions = config.get("instructions")
        tools        = config.get("tools")
        reasoner     = config.get("reasoner")
        output_requirements = config.get("output_requirements")
        self.agent_type = "ReAct"


        if(config.get('max_steps')):
            self.max_steps = config.get("max_steps")
        else:
            self.max_steps = 20
        
        
        #self.model = model
        self.role = role
        self.agent_instructions = instructions  
        if(output_requirements):
            self.output_requirements = output_requirements
        else:
            self.output_requirements = None
        self.tools = tools
        self.tool_descriptions = []
        self.km = None
        if api_key_path:
            self.km = KeyManager(api_key_path)
        else:
            self.km = KeyManager()

        if(config.get('reasoner')):
            self.reasoning = reasoner #LLM("Reasoning", model=self.model, config={"api_key": self.km.get("OPENAI_API_KEY")})
        #self.max_steps = 10
        else:
            raise Exception("Reasoner not found in config")


        self.add_actions()


    def add_tool(self, tool):
        print("Adding tool: ", tool["name"])

        properties = {}
        for param in tool["parameters"]:
            properties[param["name"]] = {
                "type": param["type"],
                "description": param["description"]
            }

        self.tool_descriptions.append({
            "type": "function", #tool["type"],
            "function": {
            "name": tool["name"],
                "description": tool["description"],
                "parameters": {
                    "type": "object",
                    "properties": properties
                }
            }
        })

        self.tools[tool["name"]] = tool["function"]



    def run_agent(self, task, write_to_file=False):

        steps = Steps()

        try:
            messages = [
                {"role": "system", "content": f"You are a {self.role} agent."},
                {"role": "user", "content": f"Your instructions for the task are : {self.agent_instructions}"},
                {"role": "user", "content": f"The inputs to the task are: {task}"},
                {"role": "user", "content": f"The tools available to you are: {self.tool_descriptions}"},
                {"role": "user", "content": f"For each tool call, explain in brief why you are calling the tool."},
                {"role": "user", "content": f"When you draft the final response to the user who provided the task, do not the reasoning behind the steps and tool calls, just producte the final response as requested by the instructions and task."}
            ]

            if(self.output_requirements):
                messages.append(
                    {
                        "role": "user", "content": f"The output requirements and formatfor the task are: {self.output_requirements}. You final response should match the output requirements and format. "
                    }
                )

            context      = []
            isCompleted  = False
            agent_output = None
            nSteps       = 0
            #steps        = []

            print("----------------------------------Tools Provided ------------------------------")
            #print("Active Tools : ")
            for tool in self.tool_descriptions:
                print(tool["function"]["name"])
            print("-------------------------------------------------------------------")
            
            while not isCompleted:

                prompt_messages = messages.copy()

                # if(len(context) > 0):
                    
                #     prompt_messages.append(
                #         {
                #             "role": "user", "content": f"Previous tool calls: {str(context)}"
                #         }
                #     )


                current_state = steps.get_current_state()
                if(len(current_state) > 0):
                    prompt_messages.append(
                        {
                            "role": "user", "content": f"Current state of the task run: {str(current_state)}"
                        }
                    )
                #print("Prompt Messages : ", prompt_messages)
                #print("Tool Descriptions : ", self.tool_descriptions)

                response = self.reasoning.call_llm(prompt_messages, self.tool_descriptions)

                steps.add_step({
                    "step": nSteps,
                    "type":"reasoner",
                    "node":"Reasoner",
                    "content": response["message"].content,
                    "finish_reason": response['finish_reason'],
                    "tool_calls": response['tool_calls']
                })

                nSteps += 1

                print("----------------------------------Reasoning " + str(nSteps) + " ------------------------------")
                print(response["message"].content)
                print("Tool Calls : ", response['tool_calls'])
                print("----------------------------------Reasoning ------------------------------")

                finish_reason = response['finish_reason']
                tool_calls    = response['tool_calls']


                if nSteps > self.max_steps:
                    print("----------------------------------Max Steps Reached ------------------------------")
                    print("Max steps reached, stopping agent.")
                    isCompleted = True
                    agent_output_str = response['message'].content
                    agent_output = {
                        "output": agent_output_str
                    }
                    print("----------------------------------Final Agent Response ------------------------------")
                    print(agent_output)
                    print("----------------------------------Final Agent Response ------------------------------")
                    break

                
                if finish_reason == "stop":
                    agent_output_str = response['message'].content
                    agent_output = {
                        "output": agent_output_str
                    }
                    isCompleted  = True
                    print("----------------------------------Final Agent Response ------------------------------")
                    print(agent_output)
                    print("----------------------------------FinalAgent Response ------------------------------")
                    break

                elif finish_reason == "tool_calls":
                    for tool_call in tool_calls:
                        tool_name = tool_call['function']['name']
                        tool_args = tool_call['function']['arguments']

                        tool_output = self.tools[tool_name](**tool_args)

                        context.append(
                            {
                                "tool_name": tool_name, 
                                "tool_output": str(tool_output)
                            }
                        )

                        steps.add_step({
                            "step": nSteps,
                            "type":"tool",
                            "node":tool_name,
                            "content": tool_output
                        })

                        print("----------------------------------Tool Response " + str(nSteps) + " | " + tool_name + " ------------------------------")
                        print(tool_output)
                        print("----------------------------------Tool Response ------------------------------")

                        nSteps += 1


            if write_to_file:
                self.export_run(task, steps.get_steps(), context, agent_output)

            # print("----------------------------------Steps ------------------------------")
            # print(steps.get_steps())
            # print("----------------------------------Steps ------------------------------")


        except Exception as e:
            print("Error in Agent: ", e)
            error_response = {
                "error": str(e),
            }
            return {
            "outputs":error_response, 
            "steps": steps.get_steps()
            }


        return {
            "outputs": agent_output,
            "steps": steps.get_steps()
        }
        


    def export_run(self, task, steps, context, agent_output):
        print("Writing Agent Run to File")


        curr_date = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"{self.name}_{curr_date}.json"

        with open(file_name, "w") as f:
            json.dump({
                "task": task,
                "steps": steps,
                "context": context,
                "agent_output": agent_output
            }, f)



    def export_model(self):

        tools = []

        for tool in self.tool_descriptions:
            newTool = {
                "type": "function",
                "name": tool["function"]["name"],
                "description": tool["function"]["description"],
                "inputs":[]
            }

            for name, value in tool["function"]["parameters"]["properties"].items():
                newTool["inputs"].append({
                    "name": name,
                    "type": value["type"],
                    "description": value["description"]
                })
            tools.append(newTool)


        agent_model = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "config":{},
            "tools": tools,
            "reasoner": {
                "model": self.reasoning.model,
            },
            "config":{
                "max_steps": self.max_steps
            }
        }
        return agent_model


    def add_actions(self):

        node_inputs = [
            {
                "name":"task",
                "type":"dict",
                "description":"The input task to the agent",
                "inputType":"input",
                "source":"",
                "value":None
            },
        ]
        node_outputs = [
            {
                "name":"outputs",
                "type":"dict",
                "description":"Outputs from the agent"
            },
            {
                "name":"steps",
                "type":"list",
                "description":"Steps taken by the agent"
            }
        ]
        self.add_action(action_name="run_agent", function=self.run_agent, parameters={}, inputs=node_inputs, outputs=node_outputs, isDefault=True, description="Run the agent")
        