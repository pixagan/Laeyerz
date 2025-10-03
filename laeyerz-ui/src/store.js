import { combineReducers } from 'redux'
import { configureStore } from '@reduxjs/toolkit';


import { currentflowReducer, flowStateReducer, dataflowReducer, currentNodeReducer } from './reducers/flowReducers'

const reducer = combineReducers({

    currentFlowR: currentflowReducer,
    flowAppStateR: flowStateReducer,
    currentNodeR: currentNodeReducer

})


const store = configureStore({reducer:reducer});


export default store