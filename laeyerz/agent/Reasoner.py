from laeyerz.flow.Node import Node
from llmbox.LLMNode import LLMNode

class Reasoner(Node):

    def __init__(self, name, config):
        super().__init__(name, {})

        print("Reasoner config: ", config)

        self.name = name
        

        self.llm = config.get('llm')


    def initialize(self, role, task, instructions, tool_descriptions, todos=None):

        self.role = role
        self.task = task
        self.instructions = instructions
        self.todos = todos
        self.tools = tool_descriptions

        self.messages =  [
            {"role": "system", "content": f"You are a {role} agent."},
            {"role": "user", "content": f"Your instructions for the task are : {instructions}"},
            {"role": "user", "content": f"The tools available to you are: {tool_descriptions}"},
            {"role": "user", "content": f"The inputs to the task are: {task}"},
            {"role": "user", "content": f"For each tool call, explain in brief why you are calling the tool."},
            {"role": "user", "content": f"When you draft the final response to the user who provided the task, do not the reasoning behind the steps and tool calls, just producte the final response as requested by the instructions and task."}
        ]



    def reason(self, steps, plan=None):
   
        prompt_messages = self.messages.copy()

        current_state = steps.copy()

        if(len(current_state) > 0):
            prompt_messages.append(
                {
                    "role": "user", "content": f"Current state of the task run: {str(current_state)}"
                }
            )

        response = self.llm.call_llm(prompt_messages, self.tools)

        content       = response["message"].content
        finish_reason = response['finish_reason']
        tool_calls    = response['tool_calls']

        tools_returned = []

        for tool_call in tool_calls:
            tool_call_id = tool_call['id']
            tool_type    = tool_call['type']
            tool_name    = tool_call['function']['name']
            tool_args    = tool_call['function']['arguments']

            tool_returned = {
                "_id": tool_call_id,
                "type": tool_type,
                "name": tool_name,
                "arguments": tool_args,
            }

            tools_returned.append(tool_returned)

        reasoner_response = {
            "content": content,
            "finish_reason": finish_reason,
            "tool_calls": tools_returned
        }

        return reasoner_response

        