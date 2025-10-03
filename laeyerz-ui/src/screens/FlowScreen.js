import React , {useEffect, useState, useCallback, act } from 'react'

import { Row, Col, Button, ListGroup, InputGroup, Card } from 'react-bootstrap'

import { useSelector, useDispatch } from 'react-redux'




import FlowViewBasic from '../components/flow/FlowViewBasic'
import AppStateView from '../components/flow/AppStateView'
import FlowMainMenu from '../components/flow/FlowMainMenu'


import axios from 'axios'

import { useParams } from 'react-router-dom'

import {
    LOAD_CURRENT_FLOW,
    CURRENT_FLOW_FAIL,
    RESET_CURRENT_FLOW,

    LOAD_APP_STATE,
    APP_STATE_FAIL,
    RESET_APP_STATE,
    UPDATE_APP_STATE

} from "../constants/flowConstants"


export const FlowScreen = ({match, history}) => {

    
    const dispatch = useDispatch()

    const currentFlowR = useSelector(state => state.currentFlowR)
    const { currentFlow } = currentFlowR

   

    const flowAppStateR = useSelector(state => state.flowAppStateR)
    const { flowAppState } = flowAppStateR
   

    const [viewMode, setViewMode] = useState('flow')
 
    const [flowTitle, setFlowTitle] = useState("Flow i")
    
 


    const loadFlow = async () => {
        const response = await axios.get(`/api/flow`)

        console.log("Response : ", response.data)
       

        dispatch({type: 'LOAD_CURRENT_FLOW', payload: {currentFlow: response.data.flow}})
    }

    



    const onMenuAction = (action, data) => {
        console.log("Menu action : ", action, data)

        switch(action){
            case 'view-graph':
                setViewMode('flow')
                break

            case 'view-state':
                setViewMode('state')
                break

          
            default:
                break
        }

    }
   
 

    useEffect(() => {
        
        loadFlow()
    }, [])

   

    return(



        <div style={{paddingTop:'0px', marginTop:'0px', height:'100vh'}}>


            <FlowMainMenu onMenuAction={onMenuAction} flowTitle={flowTitle}/>

            <Row>
                <Col>
                {viewMode == 'flow' && (
                    <>
                        <FlowViewBasic currentFlow={currentFlow}/>
                    </>
                )}

                {viewMode == 'state' && (
                    <>
                        <AppStateView appState={flowAppState}/>
                    </>
                )}
                </Col>

            </Row>

            

        </div>



    )


}

export default FlowScreen


