import React from 'react'
import { Link } from '@reach/router'

const styles = {
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
  textAlign: 'center',
  justifyContent: 'center',
  marginTop: 50
}

const NotFound = () => (
  <div css={styles}>
    <h1>Oh no!</h1>
    <br />
    <h4 className='text-muted'>
      You seem to have stumbled across a page that was or has yet to be written.
      Head back to the <Link to='/feed'>feed</Link> or try something else.
    </h4>
    <br />
    <br />
    <blockquote className='blockquote'>
      <p>"Not all those who wander are lost."</p>
      <footer className='blockquote-footer'>
        J.R.R. Tolkien, <i>The Fellowship of the Ring</i>
      </footer>
    </blockquote>
  </div>
)

export default NotFound
