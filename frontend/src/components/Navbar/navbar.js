import React from 'react'

import AuthenticationButton from './Buttons/auth-button'
import './navbar.css'


const NavBar = () => {
  
    return (
        <nav class="navBarItems nav">
            <h1 class="navbar-logo">
                <AuthenticationButton />
            </h1>
        </nav>
    )
  
  }

  export default NavBar;