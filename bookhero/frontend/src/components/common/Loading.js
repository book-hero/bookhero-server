import React from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faCog } from '@fortawesome/pro-solid-svg-icons'

const Loading = () => (
  <div className='text-primary' css={{ width: '100%', textAlign: 'center' }}>
    <FontAwesomeIcon icon={faCog} size='2x' spin />
  </div>
)

export default Loading
