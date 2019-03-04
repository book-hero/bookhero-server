import React from 'react'
import { Link } from '@reach/router'

const NavLink = props => (
  <Link
    {...props}
    getProps={({ isCurrent }) => {
      const activeClass = isCurrent ? 'active' : ''
      return {
        className: `nav-link ${activeClass}`
      }
    }}
  />
)

const NavBar = props => {
  return (
    <nav className='navbar navbar-expand-sm navbar-light bg-light'>
      <button
        className='navbar-toggler'
        type='button'
        data-toggle='collapse'
        data-target='#navbarToggler'
        aria-controls='navbarToggler'
        aria-expanded='false'
        aria-label='Toggle navigation'
      >
        <span className='navbar-toggler-icon' />
      </button>
      <div className='collapse navbar-collapse' id='navbarToggler'>
        <a className='navbar-brand' href='#'>
          Book Hero
        </a>
        <ul className='navbar-nav mr-auto mt-2 mt-lg-0'>
          <li className='nav-item'>
            <NavLink to='feed' className=''>
              Feed
            </NavLink>
          </li>
          <li className='nav-item'>
            <NavLink className='nav-link' to='discover' className=''>
              Discover
            </NavLink>
          </li>
          <li className='nav-item'>
            <NavLink className='nav-link' to='contribute' className=''>
              Contribute
            </NavLink>
          </li>
        </ul>
      </div>
    </nav>
  )
}

export default NavBar
