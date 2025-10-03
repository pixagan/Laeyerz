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
LaeyerzAPI module for API operations
in the Laeyerz framework.
"""



import os

from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

import uuid

from pydantic import BaseModel
from typing import List, Optional
import uvicorn

import datetime

from dotenv import load_dotenv
load_dotenv()



from laeyerz.flow.Flow import Flow
from laeyerz.flow.Node import Node
from laeyerz.flow.AppState import AppState


class FlowInputsRequest(BaseModel):
    flowInputs: dict




class LaeyerzVizAPI:

    def __init__(self):
        print("Initializing Laeyerz Flow Visualization")

        self.api =  FastAPI(
                                title="Flow Viz API",
                                description="Backend API for Laeyerz-Viz Application",
                                version="1.0.0"
                            )

        self.api.add_middleware(
                                    CORSMiddleware,
                                    allow_origins=["http://localhost:3221"],
                                    allow_credentials=True,
                                    allow_methods=["*"],
                                    allow_headers=["*"],
                                )

        
        self.runs = []
        self.flow = None

    
        self.setup_routes()



    def set_flow(self, flow_in):
        self.flow = flow_in


    def add_run(self, run_in):
        self.runs.append(run_in)


    def setup_routes(self):


        #----------Sessions -----------
        # Basic CRUD routes
        @self.api.get("/")
        async def root():
            return {"message": "Welcome to Laeyerz-View API"}


        #--------------- Flow -----------
    
        @self.api.get("/api/flow")
        async def get_flow():

            fd = self.flow.to_view()

            return {"flow": fd}



        @self.api.get("/api/state")
        async def get_flow_state():

            keys, fs = self.flow.state.to_view()

            return {"sections": keys, "state": fs}


        @self.api.get("/api/observe")
        async def get_metrics():

            appState = {}

            return {"appState": appState}



        @self.api.get("/api/dataflow")
        async def get_flow_state():

            appState = self.flow.state

            return {"appState": appState.state}


    #-----------------  Nodes ------------------------------------
        @self.api.get("/api/node/{node_id}")
        async def get_node_detail(node_id: str):

            node = self.flow.get_node(node_id)
            node_dict = node.to_dict()
            node_dict['actions'] = node.actions

            return {"nodeDetail": node_dict}


    #---------------------------------------------------------------


    def run(self, host = "0.0.0.0", port = 6221):
        uvicorn.run(self.api, host=host, port=port)



#------------------------------



def main():
 
    lflow = LaeyerzVizAPI()


    ## Create Functional Nodes
    simple_flow = Flow("Flow 1")

    simple_flow.state.update("Inputs", "input0", "Hello")

    def model0(input0:str)->(str):

        print("Model 0 :", input0)

        output = input0+"_model0"

        return output

    node1 = Node("Model0")
    node1.inputs  = {"Inputs:input0":"input0"}
    node1.outputs = {"output0":"Model0:output0"}
    node1.set_function(model0)
    simple_flow.add_node(node1)



    def model1(input1:str)->(str):

        print("Model 1 :", input1)

        output = input1 + "_model1"

        return output

    node2 = Node("Model1")
    node2.inputs  = {"Model0:output0":"input1"}
    node2.outputs = {"output1":"Model1:output1"}
    node2.set_function(model1)
    simple_flow.add_node(node2)


    def model2(input2:str)->(str):
        

        print("Model 2 :", input2)

        output = input2 + "_model2"

        return output

    node3 = Node("Model2")
    node3.inputs  = {"Model1:output1":"input2"}
    node3.outputs = {"output2":"Outputs:output2"}
    node3.set_function(model2)
    simple_flow.add_node(node3)



    def model3(input3:str)->(str):
        

        print("Model 3 :", input3)

        output = input2 + "Dance"

        return output

    node4 = Node("Dance")
    node4.inputs  = {"Model1:output1":"input2"}
    node4.outputs = {"output2":"Outputs:output2"}
    node4.set_function(model3)
    simple_flow.add_node(node4)




    # Add edges to define your workflow
    simple_flow.add_edge("START", "Model0")
    simple_flow.add_edge("Model0", "Model1")
    simple_flow.add_edge("Model1", "Model2")
    simple_flow.add_edge("Model1", "Dance")
    simple_flow.add_edge("Model2", "END")

    #finalize the flow - let flow make required pre computations, generate structures
    simple_flow.finalize()

    lflow.set_flow(simple_flow)

    #lflow.

    lflow.run()

if __name__ == "__main__":
    main()

