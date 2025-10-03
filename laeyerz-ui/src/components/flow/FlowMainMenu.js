import React, { useState, useEffect } from 'react'
import { Navbar, Nav, NavDropdown, Container, Button, Badge } from 'react-bootstrap'
import { 
    FileText, 
    Bot, 
    Activity, 
    Settings, 
    HelpCircle,
    Trash2,
    ClipboardPaste,
    Undo,
    Redo,
    ZoomIn,
    ZoomOut,
    Monitor,
    BarChart3,
    Cog,
    Info,
    CirclePlus,
    Workflow,
    TableProperties
} from 'lucide-react'

import { Play, Save, Copy, Download, Upload, Eye, Edit3 } from 'lucide-react';


export const FlowMainMenu = ({ onMenuAction, flowTitle }) => {
    const [activeMenu, setActiveMenu] = useState(null)

    useEffect(() => {
        // Initialize menu state
        setActiveMenu(null)
    }, [])

    const handleMenuClick = (action, data = null) => {
        if (onMenuAction) {
            onMenuAction(action, data)
        }
    }


    const runFlow = () => {
        console.log("Hello")
    }

    return (
        <Navbar bg="light" expand="lg" className="border-bottom" style={{marginTop:'0px', paddingTop:'0px', paddingBottom:'10px'}}>
            <Container fluid>
               
                    <Nav>
                    <p className='h4'>Laeyerz</p>
                    </Nav>

                    <Nav>
                        <p className='h4'>{flowTitle}</p>

                    </Nav>
                
                <Nav className="me-auto">
                
                    
                    <Nav.Link onClick={() => handleMenuClick('view-graph')}>
                        <Workflow size={16} className="me-1" />
                        Graph
                    </Nav.Link>

                    <Nav.Link onClick={() => handleMenuClick('view-state')}>
                        <TableProperties size={16} className="me-1" />
                        State
                    </Nav.Link>

                   
                  
                </Nav>

              
                
            </Container>
        </Navbar>
    )
}

export default FlowMainMenu
