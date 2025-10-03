import React , { useState, useEffect,} from 'react'
import { Navbar, Nav, Card, Badge, InputGroup, Button, Form, Container, ListGroup} from 'react-bootstrap'
import { ArrowBigDown } from 'lucide-react'
import { Pencil, Check, Activity, Bot } from 'lucide-react'
import axios from 'axios'
import { useSelector } from 'react-redux'

export const GraphItemView = ({}) => {

    const currentFlowR = useSelector(state => state.currentFlowR)
    const { currentFlow } = currentFlowR
    
    const [viewMode, setViewMode] = useState("nodes")

    const [name, setName] = useState("")
    const [nodes, setNodes] = useState([])
    const [edges, setEdges] = useState([])


    const viewGraphRequest = async() => {
        const config = {
            headers: {
                'Content-Type': 'application/json',
            }
        }

        const response = await axios.get(`/api/flow/${currentFlow.id}`, config)
        
        const data = response.data

        //console.log(data)

        console.log("Nodes : ", data.flow.nodes)
        console.log("Edges : ", data.flow.edges)

        setName(data.flow.name)
        setNodes(data.flow.nodes)
        setEdges(data.flow.edges)


       
    }

    useEffect(() => {
       
        viewGraphRequest()
        
    }, [])

  


    return (

        <div>

           <InputGroup>
                <Button variant="outline-secondary" onClick={() => setViewMode("nodes")}>Nodes</Button>
                <Button variant="outline-secondary" onClick={() => setViewMode("edges")}>Edges</Button>
           </InputGroup>

            <p className='h4'>{name}</p>

            {viewMode == "nodes" && (
                <div>
                    <p>Nodes</p>
                    <ListGroup>
                        {nodes.map((node) => (
                            <ListGroup.Item key={node.id}>{node.name}</ListGroup.Item>
                        ))}
                    </ListGroup>
                </div>
            )}

            {viewMode == "edges" && (
                <div>
                    <p>Edges</p>
                    <ListGroup> 
                        {edges.map((edge) => (
                            <ListGroup.Item key={edge.id}>{edge.label}</ListGroup.Item>
                        ))}
                    </ListGroup>
                </div>
            )}
                
        
        </div>

    )
}


export default GraphItemView        
