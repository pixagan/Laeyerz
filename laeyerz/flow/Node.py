# Created: Anil Variyar
# Flow is a graph structure to create complex data and task flows


class Node:

    def __init__(self, node_id, model=None):

        self.is_start = False
        self.is_end   = False

        self.is_input  = False
        self.is_output = False

        self.id      = node_id
        self.type    = ''
        self.model   = model


        self.inputs  = None
        self.outputs = None

        self.props = {}

        self.state   = {}
        
        self.sources = []
        self.targets = []

        self.condition = None

        
    
    


    def evaluate(self, app_state):

        outputs = self.model(app_state)

        next_node = self.targets[0]

        #print(self.id, "outputs : ", outputs, self.targets)

        print("\n")
        print("----------------------------------------------------")
        print("\n")

        return outputs, next_node
      
      
        # print("Evaluating Node : ", self.id)


        # inputs = app_state.get_params(self.props)
        
        # output = self.model.evaluate(inputs)

        
        # app_state.set_state(self.id, self.outputs, output)

  
        # if self.is_output ==  False:
        #     return output, self.targets[0]
        # else:
        #     return output, None




    def next_step(self):
        pass





class StartNode:

    def __init__(self):

        self.is_start = True
        self.sources = []
        self.targets = []


    def evaluate(self, app_state, inputs):

        print("Input Node")

        for key, value in inputs.items():
            app_state.set_state(key, value)


        outputs = {}

        next_node = self.targets[0]

        return outputs, next_node


class EndNode:

    def __init__(self):

        self.is_end = True
        self.sources = []
        self.targets = []


    def evaluate(self, app_state):

        print("Output Node")

        outputs = app_state.get_params(["Outputs"])

        print("Output Node Outputs: ", outputs) 

        return outputs




#----------------------------------------------------------------------


def main():

    #nodes

    node1 = Node("node1", "Node 1", "LLM", "gpt-4o")


    


#----------------------------------------------------------------------

if __name__ == "__main__":
    main()


#----------------------------------------------------------------------
