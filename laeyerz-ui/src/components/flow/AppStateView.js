import axios from 'axios'
import React , { useState, useEffect,} from 'react'
import { Card, Badge, InputGroup, Button, Table, Row, Col } from 'react-bootstrap'
import { ArrowBigDown } from 'lucide-react'

import { useDispatch, useSelector } from 'react-redux'

import { LOAD_APP_STATE } from '../../constants/flowConstants'

import AppStateItem from './AppStateItem'
import StateSectionView from './StateSectionView'


export const AppStateView = ({}) => {


    const dispatch = useDispatch()

    const [dataType, setDataType]     = useState('')
    const [dataSource, setDataSource] = useState('')
    const [dataValue, setDataValue]   = useState('')

    const [sections, setSections] = useState([])
    const [state, setState] = useState({})

    
    const currentFlowR = useSelector(state => state.currentFlowR)
    const { currentFlow } = currentFlowR

    const flowAppStateR = useSelector(state => state.flowAppStateR)
    const { flowAppState } = flowAppStateR



     const loadFlowsRequest = async () => {
        const response = await axios.get(`/api/state`)
        
        console.log(response.data)

        setSections(response.data.sections)
        setState(response.data.state)
    
        
    }

    useEffect(() => {

        if(currentFlow){
            loadFlowsRequest()
        }
        
    }, [])

    const tempState = [

    ]

 

    return (

        <div>
            <Card>
                <Card.Header>   
                <p className='h4'>App State</p>
                </Card.Header>
            </Card>

            <div style={{padding:'20px'}}>

            

            {sections.map((section) => (
                <Row>
                    <Col md={2}>
                        <p className='h5'>{section}</p>
                    </Col>
                    <Col>
                    
                        <StateSectionView flowAppState={state[section]} />
                    </Col>
                </Row>
            ))}
                

            </div>

 
            

            

          
        
        
        </div>

    )
}


export default AppStateView
