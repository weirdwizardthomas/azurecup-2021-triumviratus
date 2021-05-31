import React from 'react'
import imgsrc from '../pics/sadshroom.png'
import { Image } from 'react-bootstrap'

import {
    Switch,
    Route
} from 'react-router-dom';

//componenets
import Navigation from './Navigation'

//import App from './App'
import About from './About.js';
import ShroomFinder from './ShroomFinder.js';
import Other from './Other.js';


const App = () => {

    return (
        <div className="main">
            <Navigation />
            <Switch>
                <Route path="/" component={App} exact>
                    <div className="d-flex flex-column align-items-center">
                        <h1 style={{ color: "white" }}>Home</h1>
                        <p style={{ color: "white", fontSize: "large" }}> Omlouváme se, musíme to opravit</p>
                        <Image src={imgsrc} alt="pic" style={{ height: "45%", width: "45%" }} id="pic" />
                    </div>
                </Route>
                <Route path="/About" component={About}></Route>
                <Route path="/ShroomFinder" component={ShroomFinder}></Route>
                <Route path="/Other" component={Other}></Route>
            </Switch>

        </div>
    );

}

export default App