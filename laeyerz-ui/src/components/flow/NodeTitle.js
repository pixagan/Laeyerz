import React , { useState, useEffect,} from 'react'
import { Card, Badge, InputGroup, Button, Form} from 'react-bootstrap'
import { ArrowBigDown } from 'lucide-react'
import { Pencil, Check } from 'lucide-react'
import axios from 'axios'


export const NodeTitle = ({currentNode, updateNodeTitle}) => {


    const [viewMode, setViewMode] = useState('view')
    const [nodeTitle, setNodeTitle] = useState('')

  

    

    useEffect(() => {
        setNodeTitle(currentNode.name)
        
    }, [currentNode])

 


    return (

        <div>

            <Card>
                <Card.Header>

                  
                        <p className='h4'><span style={{color:'blue'}}>Node Title : </span>{nodeTitle}<span><Pencil onClick={() => setViewMode(viewMode === 'view' ? 'edit' : 'view')} /></span></p>
                   
                </Card.Header>
            </Card>
          
        
        
        </div>

    )
}


export default NodeTitle
