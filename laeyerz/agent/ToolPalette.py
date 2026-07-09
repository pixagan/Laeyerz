from laeyerz.flow.Node import Node

class ToolPalette(Node):

    def __init__(self, name, config):
        super().__init__(name)

        self.name = name
        self.config = config
        self.tools = []
        self.tool_descriptions = []
        self.tool_list = []

        if config.get("tools"):
            self.tools = config.get("tools")
        else:
            self.tools = {}



    def add_tools(self, tools):

        for tool in tools:
            self.add_tool(tool)
        

    def add_tool(self, tool):

        properties = {}
        for param in tool["inputs"]:
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

        self.tool_list.append({
            "name": tool["name"],
            "description": tool["description"]
        })



    def get_tool_descriptions(self):
        return self.tool_descriptions



    def run_tool(self, tool_name, tool_args):

        tool_output = None
        tool_response = {}

        try:
            tool_output = self.tools[tool_name](**tool_args)
            tool_response["tool_name"] = tool_name
            tool_response["output"] = tool_output
            tool_response["status"] = "success"
            tool_response["error"] = None
            
            return tool_response

        except Exception as e:
            tool_response["tool_name"] = tool_name
            tool_response["output"] = None
            tool_response["status"] = "error"
            tool_response["error"] = e

            return tool_response

            #return f"Error running tool {tool_name}: {e}"

       