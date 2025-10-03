import axios from 'axios'
import React , { useState, useEffect,} from 'react'
import { Card, Badge, InputGroup, Button, Table, Row, Col } from 'react-bootstrap'
import { ArrowBigDown } from 'lucide-react'

import { useDispatch, useSelector } from 'react-redux'

import { LOAD_APP_STATE } from '../../constants/flowConstants'


export const StateSectionView = ({flowAppState}) => {


    const dispatch = useDispatch()

   

    const [sections, setSections] = useState([])
   

    

    useEffect(() => {

       
        
    }, [])

    const tempState = [

    ]

 

    return (

        <div>
            
                <Table>
                
                <tbody>
                    <tr>
                        <td className="h5" style={{padding:'10px'}}>Type/Node</td>
                        <td className="h5" style={{padding:'10px'}}>Name</td>
                        <td className="h5" style={{padding:'10px'}}>Type</td>
                        <td className="h5" style={{padding:'10px'}}>Value</td>
                    </tr>
                    {flowAppState && Object.keys(flowAppState).length > 0 && Object.keys(flowAppState).map((key) => (
                    <>
                    <tr>
                        <td>Shared</td>
                        <td>{key}</td>
                        <td>type</td>
                        <td>{flowAppState[key]}</td>
                    </tr>
                    
                    </>
                    
                    ))}
                </tbody>
            </Table>
          
        
        
        </div>

    )
}


export default StateSectionView
