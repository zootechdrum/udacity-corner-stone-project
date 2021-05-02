import { Divider } from '@material-ui/core'
import React from 'react'

import AuthenticationButton from './Buttons/auth-button'
import './navbar.css'


const NavBar = () => {
  
    return (
        <nav class="navBarItems nav">
            <div class="navbar-logo">
                <AuthenticationButton />
            </div>
        </nav>
    )
  
  }

  export default NavBar;