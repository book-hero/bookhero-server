import React from 'react'
import Profile from './Profile'
import { Router, Redirect } from '@reach/router'
import Feed from '../pages/Feed'
import Discover from '../pages/Discover'
import Contribute from '../pages/Contribute'
import NotFound from '../pages/NotFound'

const Main = props => (
  <div className='container-fluid'>
    <div className='row'>
      <div id='leftColumn' className='col-3'>
        <Profile />
      </div>
      <div id='middleColumn' className='col'>
        <Router>
          <Redirect noThrow from='/' to='feed/' />
          <Feed path='feed/' />
          <Discover path='discover/' />
          <Contribute path='contribute/' />
          <NotFound default />
        </Router>
      </div>
      <div id='rightColumn' className='col-3'>
        Right
      </div>
    </div>
  </div>
)

export default Main
