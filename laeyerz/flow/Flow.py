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
Flow module for managing workflow execution
in the Laeyerz framework.
"""
import uuid
import json

from laeyerz.flow.Node import Node  
from laeyerz.flow.AppState import AppState
from laeyerz.flow.Edge import Edge
from laeyerz.flow.Evals import Evals
from laeyerz.flow.Observe import Observe

class Flow:

    def __init__(self,name=""):

        self.id             = ""
        self.name           = name
        self.description    = ""
        
        self.nodes          = []
        self.node_map       = {}
        self.node_id_map    = {}

        self.edges          = []
        self.edge_map       = {}
        
        self.state          = AppState()
        self.observe        = Observe()

        self.components     = {}
        self.components_map = {}
        self.flowtype = "workflow"  # agent

        self.start = None
        self.end   = None

        self.max_steps = 50

        self.output = "final_output"

        self.steps = []


    def create(self, flow_name):

        self.name = flow_name
        self.id   = str(uuid.uuid4())


    def get_node(self, node_id):

        for node in self.nodes:
            if(node.id == node_id):
                return node

        return None



    def set_flow(self, flow_in):

        self.id = flow_in["id"]
        self.name = flow_in["name"]
        self.description = flow_in["description"]

        for node in flow_in["nodes"]:
            newNode = Node(node)
            self.nodes.append(newNode)




    def load_file(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data


    def create_node(self, title, function_in):
        newNode = Node(title)
        newNode.set_function(function_in)
        self.nodes.append(newNode)
        return newNode


    def add_node(self, node):

        self.nodes.append(node)
        self.node_map[node.name]  = self.nodes.index(node)
        self.node_id_map[node.id] = self.nodes.index(node)

        self.state.add_section(node.name)


        # component = component_mapping(node.component_name)
        # if(component.name not in self.components.keys()):
        #     self.components[component.name] = component
        
        # self.appflow.add_node("Embedding_Model", embedding_function)


    def run_node(self, node_id, inputs):
        
        outputs, next_node = self.nodes[self.node_id_map[node_id]].run(inputs)

        return outputs


    def delete_node(self, node_id):

        if(node_id == self.start):
            self.start = None
            return True

        if(node_id == self.end):
            self.end = None
            return True

        index = 0
        for node in self.nodes: 
            print("Match node : ", node.id, node_id)
            if(str(node.id) == str(node_id)):
                print("Removing node : ", node.id, node.name)
                self.nodes.remove(node)
                self.state.delete_node(node_id)
                print("Removed node : ", node.id, node.name)
                return True
            index += 1

        return False


    def set_action(self, component, action):

        action_function = self.components[component].get_action(action)

        #check if component has the action
        self.appflow.set_action()



    def update_node_title(self, node_id, title):
        self.nodes[self.node_id_map[node_id]].name = title

        return self.nodes[self.node_id_map[node_id]].to_dict()



    def get_node_state(self, node_id):
        return self.nodes[self.node_id_map[node_id]].state


    def finalize(self):
        print("Finalizing Flow : ")


    def add_edge(self, node1, node2):

        #check node exists
        node1_name = ""
        node2_name = ""
       

        if(node1 == 'START'):
            self.start = node2
            #self.start_node.targets.append(node_1)

            self.nodes[self.node_map[node2]].sources.append('START')
            node1_name = node1
            cNode2 = self.nodes[self.node_map[node2]]
            node2_name = cNode2.name

            #self.nodes[self.node_map[node2]].inputs.append("inputs")





        if(node2 == 'END'):
            self.end = node1
            #self.end_node.sources.append(node_0)
            #self.end_node.targets.append('END_NODE')

            self.nodes[self.node_map[node1]].targets.append('END')

            cNode1 = self.nodes[self.node_map[node1]]
            node1_name = cNode1.name
            node2_name = node2



        if(node1 != 'START' and node2 != 'END' and node1 != node2):
            self.nodes[self.node_map[node1]].targets.append(node2)
            self.nodes[self.node_map[node2]].sources.append(node1)
        
            cNode1 = self.nodes[self.node_map[node1]]
            node1_name = cNode1.name
            cNode2 = self.nodes[self.node_map[node2]]
            node2_name = cNode2.name

        newEdge = Edge(node1, node2, node1_name+"-"+node2_name)

        self.edges.append(newEdge)   

        return newEdge.to_dict()

       
    def delete_edge(self, edge_id):

        for edge in self.edges:
            print("Match edge : ", edge.id, edge_id)
            if(str(edge.id) == str(edge_id)):
                print("Removing edge : ", edge.id, edge.label)

                print(edge.to_dict())

                #remove connection from nodes
                if(edge.source != "START" and edge.target != "END"):
                    self.nodes[self.node_map[edge.source]].targets.remove(edge.target)
                    self.nodes[self.node_map[edge.target]].sources.remove(edge.source)
                    self.edges.remove(edge)
                    return True

                if(edge.source == "START"):
                    self.start = None
                    self.nodes[self.node_map[edge.target]].sources.remove(edge.source)
                    self.edges.remove(edge)

                    #update app state

                    return True
                
                if(edge.target == "END"):
                    self.end = None
                    self.nodes[self.node_map[edge.source]].targets.remove(edge.target)
                    self.edges.remove(edge)
                    return True



                

        return False
        

    def set_node_action(self, node_id, action_name):
        self.nodes[self.node_id_map[node_id]].set_action(action_name)
        return action_name


    def visualize(self):
        self.appflow.visualize()


    def run(self, input_data):

        self.steps = []

        for key, value in input_data.items():
            self.state.update('Inputs',key, value)

        curr_node = self.nodes[self.node_map[self.start]]

        nSteps = 0

        print("------------------------------------------------")
        print("-------------- Starting Flow : ", self.name)
        print("------------------------------------------------")


        
        while curr_node is not None:

            print("Evaluating Node : ", curr_node.id)
            
            outputs, next_node   = curr_node.run(self.state)

            print("Node : ",curr_node.name, outputs, next_node)

            print("State : ", self.state)

            self.steps.append({
                "type": "node",
                "node_id": curr_node.id,
                "node_name": curr_node.name,
                "node_output": outputs,
                "text":""
            })

            print(" ------------------------------------------------ ")

            nSteps += 1

            if nSteps > self.max_steps:
                break

            if(next_node != 'END'):
                curr_node = self.nodes[self.node_map[next_node]]
            else:
                break


        flow_output = self.state.get_section('Outputs')

        #print("Flow Output : ", self.output, flow_output)

        #flow_output = self.end_node.evaluate(self.appState)

        return flow_output



    def to_dict(self):

        nodes_str = []
        for node in self.nodes:
            nodes_str.append(node.to_dict())
        
        edges_str = []
        for edge in self.edges:
            edges_str.append(edge.to_dict())
        
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "nodes": nodes_str, 
            "edges": edges_str,
            "state": {}
            }


    def to_view(self):

        nodes_str = []

        startNode = {
          "id": 'START',
          "name": 'START',
          "node_id": 'START',
          "component": 'TextInput',
          "data": { 
            "label": 'START',
            "action": 'START-FLOW'
          },
          "type": 'cNode',
          "position": { "x": 0, "y": 0 },
          "inputs": ['text'],
          "outputs": ['text'],
          "code": 'print("Hello, World!")',
          "state": 'idle',
          "action": 'chatInput',
          "style": {
            "backgroundColor": "#e3d274",
          }
        }

        nodes_str.append(startNode)

        x_str = 0. + 10.0
        y_str = 0. + 70.0

        for node in self.nodes:

            newNode = {
                "id": node.name,
                "node_id": node.id,
                "name": node.name,
                "component": 'General',
                "data": { 
                    "label": node.name,
                    "action": 'UPDATE'
                },
                "type": 'cNode',
                "position": { "x": x_str, "y": y_str },
                "inputs": node.inputs,
                "outputs": node.outputs,
                "state": 'idle',
                "action": 'chatInput',
                "style": {
                    "backgroundColor": "#e3d274",
                }
                }
            nodes_str.append(newNode)

            x_str = x_str + 10.0
            y_str = y_str + 70.0
        
        

        endNode = {
          "id": 'END',
          "name": 'END',
          "node_id": 'END',
          "component": 'TextInput',
          "type": 'cNode',
          "position": { "x": x_str, "y": y_str },
          "data": { 
            "label": 'END',
            "action": 'END-FLOW'
          },
          "style": {
            "backgroundColor": "#e3d274",
          }
        }

        nodes_str.append(endNode)

        for node in nodes_str:
            print("--------------------------------")
            print("Node : ", node)
            print("--------------------------------")



        edges_str = []

        for edge in self.edges:
            edges_str.append(edge.to_dict())
        
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "nodes": nodes_str, 
            "edges": edges_str,
            "state": {}
            }


    def export_flow(self):

        return self.to_dict()




    def finalize_flow(self):
        for node in self.nodes:
            node.finalize()


    def validate_flow(self):
        for node in self.nodes:
            node.validate()


    def view(self):
        pass
        




def main():

    flow = Flow()


if __name__ == "__main__":
    main()