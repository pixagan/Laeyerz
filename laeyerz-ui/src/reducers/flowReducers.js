import {
    LOAD_CURRENT_FLOW,
    CURRENT_FLOW_FAIL,
    RESET_CURRENT_FLOW,

    LOAD_APP_STATE,
    APP_STATE_FAIL,
    RESET_APP_STATE,
    UPDATE_APP_STATE

} from "../constants/flowConstants"


 export const currentflowReducer = (state = { currentFlow : null}, action) => {

    switch(action.type){

        case LOAD_CURRENT_FLOW:
            return { loading: false, currentFlow: action.payload.currentFlow }

        case RESET_CURRENT_FLOW:
            return { loading: false, currentFlow: null }

        case CURRENT_FLOW_FAIL:
            return { loading: false, currentFlow: state.currentFlow }

        default:
            return state
    }

}




export const flowStateReducer = (state = { flowAppState : {}}, action) => {

    switch(action.type){

        case LOAD_APP_STATE:
            return { loading: false, flowAppState: action.payload }

        case UPDATE_APP_STATE:
            return { loading: false, flowAppState: action.payload }


        case RESET_APP_STATE:
            return { loading: false, flowAppState: null }

        case APP_STATE_FAIL:
            return { loading: false, flowAppState: state.flowAppState }

        default:
            return state
    }

}




export const currentNodeReducer = (state = { currentNode : null}, action) => {

    switch(action.type){

        case LOAD_CURRENT_FLOW:
            return { loading: false, currentNode: action.payload.currentNode }

        case RESET_CURRENT_FLOW:
            return { loading: false, currentNode: null }

        case CURRENT_FLOW_FAIL:
            return { loading: false, currentNode: state.currentNode }

        default:
            return state
    }

}