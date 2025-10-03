import axios from 'axios'
import React , { useState, useEffect, useRef} from 'react'
import { Card, Badge, InputGroup, Button, ButtonGroup, Form } from 'react-bootstrap'
import { ArrowBigDown } from 'lucide-react'

import { Settings, Play, Save, Copy, Download, Upload, Eye, Edit3, TableProperties, Waypoints, CodeXml } from 'lucide-react';


export const NodeViewBasic = ({currentNode}) => {


    const [nodeDetail, setNodeDetail] = useState({})
   


    const loadNodeDetailRequest = async (node_id) => {

        
        const response = await axios.get(`/api/node/${node_id}`)
        const data = response.data
        console.log(data)
        setNodeDetail(data.nodeDetail)

    }


  
    
    
    useEffect(() => {
        
        loadNodeDetailRequest(currentNode.node_id)
    }, [currentNode])




    return (

        <div>

            <Card>
                <Card.Header>
                    <p className="text-center h3">{currentNode.name}</p>
                </Card.Header>
            </Card>
           
           

            


        
        
        </div>

    )
}


export default NodeViewBasic
