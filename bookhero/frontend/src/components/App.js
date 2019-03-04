import '@babel/polyfill'
import React from 'react'
import NavBar from './layout/NavBar'
import Main from './layout/Main'
import { Provider } from 'react-redux'
import { store } from '../redux/'

export default class App extends React.Component {
  render () {
    return (
      <Provider store={store}>
        <NavBar />
        <Main />
      </Provider>
    )
  }
}
