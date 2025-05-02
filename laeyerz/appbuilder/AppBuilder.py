class AppBuilder:

    def __init__(self):
        self.flow = Flow()


    def add_node(self, nodetype, params):

        model = None
        error = None

        if(nodetype == "LLM"):
            model =  LLMNode(params)

        else if(nodetype == "Embedding"):
            model = EmbeddingNode(params)

        else if(nodetype == "VectorDB"):
            model = VectorDBNode(params)

        else:
            model = None
            error = "Invalid Node type"

        if(model is not None):
            self.flow.add_node(model)

        else:
            raise ValueError(error)



 
    def add_edge(self, node1, node2):

        compatibility = self.check_compatibility(node1, node2)

        if(compatibility == True):
            self.flow.add_edge(node1, node2)

        else:   
            raise ValueError("Incompatible nodes")




    def check_compatibility(self, node):


        pass



    
    def remove_node(self, node):

        #remove relevant edges
        pass



    def remove_edge(self, edge):

        #check if edge exists

        pass

        

    def finalize(self):

        self.flow.finalize()
        pass



    def load_flow_from_file(self, flow_id):
        self.flow = Flow()



    def export_flow_to_file(self, flow_id):
        pass

# ------------------------------------------------------------------

def main():

    appbuild = AppBuilder()
    
    
    appbuild.add_node("LLM", {})
    appbuild.add_node("Embedding", {})
    appbuild.add_node("VectorDB", {})
    appbuild.add_node("DataParser", {})
    appbuild.add_node("TextOutput", {})


    appbuild.add_edge("LLM", "Embedding")
    appbuild.add_edge("Embedding", "VectorDB")
    appbuild.add_edge("VectorDB", "DataParser")
    appbuild.add_edge("DataParser", "TextOutput")


    appbuild.finalize()




#----------------------------------------------------------------------

if __name__ == "__main__":
    main()


#----------------------------------------------------------------------
