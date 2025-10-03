import axios from 'axios'
import React , { useState, useEffect,} from 'react'
import { Card, Badge, InputGroup, Button, Table } from 'react-bootstrap'
import { ArrowBigDown } from 'lucide-react'

import { useDispatch, useSelector } from 'react-redux'

import { LOAD_APP_STATE } from '../../constants/flowConstants'

import AppStateItem from './AppStateItem'


export const AppStateView = ({currentNode, appState}) => {


    const dispatch = useDispatch()

    const [dataType, setDataType] = useState('')
    const [dataSource, setDataSource] = useState('')
    const [dataValue, setDataValue] = useState('')

    
    const currentFlowR = useSelector(state => state.currentFlowR)
    const { currentFlow } = currentFlowR

    const flowAppStateR = useSelector(state => state.flowAppStateR)
    const { flowAppState } = flowAppStateR



    useEffect(() => {

       
        
    }, [])

  

 

    return (

        <div>
            <Card>
                <Card.Header>   
                <p className='h4'>App State</p>
                </Card.Header>
            </Card>


            


            

            <table>
                <thead>
                    <tr>
                        <td className="h5" style={{padding:'10px'}}>Key</td>
                        <td className="h5" style={{padding:'10px'}}>Value</td>
                    </tr>
                </thead>
                <tbody>
            {flowAppState && Object.keys(flowAppState).length > 0 && Object.keys(flowAppState).map((key) => (
               <>
               <AppStateItem flow_id={currentFlow.id} ckey={key} cvalue={flowAppState[key]}/>
               </>
              
            ))}
            </tbody>
            </table>
            

            

          
        
        
        </div>

    )
}


export default AppStateView
