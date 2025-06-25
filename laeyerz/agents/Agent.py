
import laeyerz.llms.LLMx as LLMx
import laeyerz.memory.AgentMemory as AgentMemoryST


## When you create an agent , keep it simple and focussed on a specific task.
## Use Flows to build complex LLM powered systems

class Agent:

    def __init__(self, name, description, llm, tools):

        self.name        = name
        self.description = description
        self.llm         = llm
        self.tools       = tools
        self.memoryST    = AgentMemoryST()
        self.memoryDICT  = {}
        self.flow        = None
        self.model       = model
        


    def evaluate(self, task):

        messages = []
        tools    = self.tools

        while True:

            response = llm.run(model, messages, tools)
            
            if(response.call_tool == True):
                for tool in response.tool_calls:
                    self.tools[tool.name].run(tool.args)

            if(response.message == "END"):
                break


        #Get final response

        return response





#----------------------------------------------------------------------


def main():

    agent = Agent()
   

#----------------------------------------------------------------------

if __name__ == "__main__":
    main()


#----------------------------------------------------------------------



