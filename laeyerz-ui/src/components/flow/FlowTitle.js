import React , { useState, useEffect,} from 'react'
import { Navbar, Nav, Card, Badge, InputGroup, Button, Form, Container} from 'react-bootstrap'
import { ArrowBigDown } from 'lucide-react'
import { Pencil, Check, Activity, Bot } from 'lucide-react'


export const FlowTitle = ({flowTitle, updateFlowTitle}) => {


    const [viewMode, setViewMode] = useState('view')
    const [nodeTitle, setNodeTitle] = useState("")

    

    useEffect(() => {
        setNodeTitle(flowTitle)
        
    }, [flowTitle])

    const updateNodeTitle = (title) => {
        updateFlowTitle(title)
    }

 


    return (

        <div>

            <Navbar bg="light" expand="lg" className="border-bottom" style={{marginTop:'0px', paddingTop:'0px', paddingBottom:'10px'}}>

            <Container fluid>
                <Navbar.Brand className="fw-bold text-primary">
                    Laeyerz
                </Navbar.Brand>
                <Nav className="me-auto">
                {viewMode === 'view' ? (
                        <p className='h4'><span style={{color:'blue'}}>Project Title : </span>{nodeTitle}<span><Pencil onClick={() => setViewMode(viewMode === 'view' ? 'edit' : 'view')} /></span></p>
                    ) : (
                        <InputGroup>
                            <Form.Control type="text" value={nodeTitle} onChange={(e) => updateNodeTitle(e.target.value)} />
                            <Button onClick={() => setViewMode(viewMode === 'view' ? 'edit' : 'view')} style={{marginLeft:'10px', backgroundColor:'blue', color:'white' }}><Check /></Button>
                        </InputGroup>
                    )}
                </Nav>

                </Container>
            </Navbar>

                
                
        
        </div>

    )
}


export default FlowTitle
