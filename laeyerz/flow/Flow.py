# Created: Anil Variyar
# Flow is a graph structure to create complex data and task flows

import json

from laeyerz.flow.Edge import Edge
from laeyerz.flow.Node import Node
from laeyerz.flow.AppState import AppState

from laeyerz.flow.Node import StartNode, EndNode

class Flow:
    
    def __init__(self):

        self.nodes = []
        self.edges = []

        self.start_node = StartNode()
        self.end_node   = EndNode()

        self.start = 0
        self.stack = []
        self.state = {}
        self.appState = AppState()
        self.start = None
        self.is_finalized = False


        self.node_map = {}
        self.edge_map = {}



    def add_node(self, node_id, model):

        new_node          = Node(node_id, model)

        self.nodes.append(new_node)

        self.node_map[new_node.id] = len(self.nodes) - 1



    def add_edge(self, edge_0, edge_1, condition=None):

        #create the relevant edge
        new_edge = Edge(edge_0, edge_1, condition)

        self.edges.append(new_edge)

        #then add it to the edges list



    def delete_node(self, node):

        #remove the node from the nodes list
        if(not self.is_finalized):
            self.nodes.remove(node)



        else:
            raise ValueError("Flow is finalized")



    def remove_edge(self, edge):

        #remove the edge from the edges list
        if(not self.is_finalized):
            self.edges.remove(edge)

        else:
            raise ValueError("Flow is finalized")




    def finalize(self):

        self.assign_edge_to_nodes()


        # for edge in self.edges:    

        #     self.nodes[self.node_map[edge.node_0]].targets.append(self.nodes[self.node_map[edge.node_1]])
            
        #     self.nodes[self.node_map[edge.node_1]].sources.append(self.nodes[self.node_map[edge.node_0]])

        #finalize the flow

        #check if the flow is valid


    def assign_edge_to_nodes(self):

        for edge in self.edges:

            node_0 = edge.node_0
            node_1 = edge.node_1
            
            if(node_0 == 'START'):
                self.start = node_1
                self.start_node.targets.append(node_1)

                self.nodes[self.node_map[node_1]].sources.append(node_0)

            if(node_1 == 'END'):
                self.end = node_0
                self.end_node.sources.append(node_0)
                #self.end_node.targets.append('END_NODE')

                self.nodes[self.node_map[node_0]].targets.append('END_NODE')


            if(node_0 != 'START' and node_1 != 'END'):
                self.nodes[self.node_map[node_1]].sources.append(node_0)
                self.nodes[self.node_map[node_0]].targets.append(node_1)
            
            


    def evaluate(self, input_data):

        #get the node from the stack
        outputs, next_node = self.start_node.evaluate(self.appState, input_data)

        curr_node = self.nodes[self.node_map[next_node]]

        

        while curr_node is not None:

            print("Evaluating Node : ", curr_node.id)

            outputs, next_node = curr_node.evaluate(self.appState)


            if(next_node != 'END_NODE'):
                curr_node = self.nodes[self.node_map[next_node]]
            else:
                break


        flow_output = self.end_node.evaluate(self.appState)

        return flow_output



    def export_state(self):

        return self.state




    def add_nodes(self, nodes):

        #create the relevant node

        #then add it to the nodes list

        if(not self.is_finalized):
            self.nodes.extend(nodes)

            for inode in range(0, len(self.nodes)):
                self.node_map[self.nodes[inode].id] = inode

        else:
            raise ValueError("Flow is finalized")



    def add_edges(self, edges):

        #update the node to know its sources and targets

        #then add it to the edges list
        if(not self.is_finalized):
            self.edges.extend(edges)

        else:
            raise ValueError("Flow is finalized")




    def import_flow(self, filename):

        with open(filename, 'r') as f:
            model = json.load(f)   

        self.app_name = model['app_name']
        self.nodes = model['nodes']
        self.edges = model['edges']

        self.node_map = {}
        self.edge_map = {}
        



    def export_flow(self, filename):

        model = {
            'app_name': self.app_name,
            'nodes': self.nodes,
            'edges': self.edges
        }

        with open(filename, 'w') as f:
            json.dump(model, f)



# ------------------------------------------------------------------

def main():

    appflow = Flow()

    


#----------------------------------------------------------------------

if __name__ == "__main__":
    main()


#----------------------------------------------------------------------

