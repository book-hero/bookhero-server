import { createStore, combineReducers, applyMiddleware } from 'redux'
// import { stateKey, reducers as studentsReducer } from './students'
import logger from 'redux-logger'

const reducer = combineReducers({})

const initialState = {}

const middleware = applyMiddleware(logger)

export const store = createStore(reducer, initialState, middleware)
