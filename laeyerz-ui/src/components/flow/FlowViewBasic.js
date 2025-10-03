import React , { useState, useEffect, useCallback} from 'react'
import { Card, Badge, InputGroup, Button, Form, ListGroup, Row, Col} from 'react-bootstrap'
import { ArrowBigDown } from 'lucide-react'
import { Pencil, Check, CirclePlus } from 'lucide-react'

import axios from 'axios'

import { useSelector, useDispatch } from 'react-redux'

import { ReactFlow, Controls, Background, MiniMap, MarkerType } from '@xyflow/react';
import { applyEdgeChanges, applyNodeChanges } from '@xyflow/react';
import { addEdge } from '@xyflow/system';
import '@xyflow/react/dist/style.css';

import { CNode } from '../rflow/CNode'
import { X } from 'lucide-react'
import FlowMainMenu from './FlowMainMenu'


import NodeViewBasic from './NodeViewBasic'


export const FlowViewBasic = ({currentFlow}) => {


    const dispatch = useDispatch()

    
  



    const [flowTitle, setFlowTitle] = useState("Flow i")
    const [selectedNode, setSelectedNode] = useState(null)
    const [viewSettings, setViewSettings] = useState(false)


    const nodeTypes = {
        cNode: CNode,
    };

   

    const initialEdges = [

      ];
       
      const initialNodes = [
        {
          id: 'START',
          name: 'START',
          component: 'TextInput',
          data: { 
            label: 'START',
            action: 'START-FLOW'
          },
          type: 'cNode',
          position: { x: 0, y: 0 },
          inputs: ['text'],
          outputs: ['text'],
          code: 'print("Hello, World!")',
          state: 'idle',
          action: 'chatInput',
          style: {
            "backgroundColor": "#e3d274",
          }
        },
        {
          id: 'END',
          name: 'END',
          component: 'TextInput',
          type: 'cNode',
          position: { x: 50, y: 50 },
          data: { 
            label: 'END',
            action: 'END-FLOW'
          },
          style: {
            "backgroundColor": "#e3d274",
          }
        }
      ];
      

    const [nodes, setNodes] = useState(initialNodes);
    const [edges, setEdges] = useState(initialEdges);
    

   

    const onNodesChange = useCallback(
        (changes) => {
            console.log('Node changes : ', changes)

          

            setNodes((nds) => applyNodeChanges(changes, nds))
            
        },
        [],
      );

     

    const onEdgesChange = useCallback(
        (changes) => {
            console.log('Edge changes : ', changes)
           

            setEdges((eds) => applyEdgeChanges(changes, eds))
        },
        [],
    );




    const onNodeClick = (event, node) => {
        console.log('click node', node);
        
        //setViewSettings(viewSettings=> !viewSettings)

    }

    const onNodeDoubleClick = (event, node) => {
        console.log('double click node', node);
        setSelectedNode(node)
        setViewSettings(true)

    }


    const addEdgeRequest = (connection) => {
        const newEdge = {
            id: connection.id || `edge-${Date.now()}`,
            source: connection.source,
            target: connection.target,
            label: `${connection.source}-${connection.target}`,
            markerEnd: {
                type: MarkerType.ArrowClosed,
                width: 20,
                height: 20,
                color: '#FF0072',
            },
            style: {
                strokeWidth: 2,
                stroke: '#FF0072',
            }
        };
        
        setEdges((eds) => addEdge(newEdge, eds));
        
    }
    const loadEdges = (edges) => {
        console.log("Loading edges from backend:", edges);
        
        const formattedEdges = edges.map(edge => ({
            id: edge.id,
            source: edge.source,
            target: edge.target,
            label: edge.label,
            markerEnd: {
                type: MarkerType.ArrowClosed,
                width: 20,
                height: 20,
                color: '#FF0072',
            },
            style: {
                strokeWidth: 2,
                stroke: '#FF0072',
            }
        }));
        
        setEdges(formattedEdges);
    };


    useEffect(() => {

        if(currentFlow != null){
            if (currentFlow.nodes){
                setNodes(currentFlow.nodes)
            }
            if(currentFlow.edges){
            //setEdges(currentFlow.edges)
                loadEdges(currentFlow.edges)
            }
        }

    }, [currentFlow])

   
 


    return (

        <div>
          
  
         

            <Row>

         

                <Col >

                <div style={{ width: '100%', height: '100vh', position: 'relative' , borderWidth:'1px'}}>
                <ReactFlow nodes={nodes}
                onNodesChange={onNodesChange}
                edges={edges}
                onEdgesChange={onEdgesChange}
                onConnect={addEdgeRequest}
                onNodeClick={onNodeClick}
                onNodeDoubleClick={onNodeDoubleClick}
                nodeTypes={nodeTypes}
                style={{
                    width: '100%',
                    height: '100%',
                    background: '#fff'
                    
                }}
                fitView  
                >
                    {/* <MiniMap /> */}
                    <Background />
                    <Controls />
                </ReactFlow>
            </div>
                    
                
                </Col>

                {selectedNode && (
                    <Col style={{maxWidth:'40vw', border:'solid', borderWidth:'1px'}}>
                        
                    
                        <Button  style={{paddingTop:'2px', paddingBottom:'2px', backgroundColor:'blue', color:'white', backgroundColor:'red', alignSelf:'right'}} onClick={()=>setSelectedNode(null)}><X /></Button>
                        

                        <NodeViewBasic currentNode={selectedNode}/>
                
                     </Col>
                )}

            </Row>

         
        
        </div>

    )
}


export default FlowViewBasic
