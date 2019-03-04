import { createStore, combineReducers, applyMiddleware } from 'redux'
import logger from 'redux-logger'

const reducer = combineReducers({})

const initialState = {}

const middleware = applyMiddleware(logger)

export const store = createStore(reducer, initialState, middleware)
