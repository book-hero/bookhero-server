import React, { useRef, useState, useEffect } from 'react'
import Profile from './Profile'
import { Router, Redirect } from '@reach/router'
import Feed from '../pages/Feed'
import Discover from '../pages/Discover'
import Contribute from '../pages/Contribute'
import NotFound from '../pages/NotFound'

const middleColumnStyle = {
  overflowY: 'auto'
}

const Main = props => {
  return (
    <div className='container-fluid' id='main'>
      <div className='row'>
        <div id='leftColumn' className='column col-3'>
          <Profile />
        </div>
        <div id='middleColumn' className='column col' css={middleColumnStyle}>
          <Router>
            <Redirect noThrow from='/' to='feed/' />
            <Feed path='feed/' />
            <Discover path='discover/' />
            <Contribute path='contribute/' />
            <NotFound default />
          </Router>
        </div>
        <div id='rightColumn' className='column col-3'>
          Right
        </div>
      </div>
    </div>
  )
}

export default Main
