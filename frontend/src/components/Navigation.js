import React from 'react';
import {Button, Nav} from 'react-bootstrap'

import {
    NavLink//, 
    // Switch,
    // Route
} from 'react-router-dom';

// Components
// import App from './App'
// import About from './About.js';
// import ShroomFinder from './ShroomFinder.js';
// import Other from './Other.js';


const Navigation = () => {
    return (
        <div className="main">
            <Nav className="justify-content-center">
                <NavLink to="/"><Button variant="outline-dark" align="center">Home</Button></NavLink>
                <NavLink to="/About"><Button variant="outline-dark" align="center">About</Button></NavLink>
                <NavLink to="/ShroomFinder"><Button variant="outline-dark" align="center">Shroom finder</Button></NavLink>
                <NavLink to="/Other"><Button variant="outline-dark" align="center">Other</Button></NavLink>
            </Nav>
        </div>
    );
}

export default Navigation;