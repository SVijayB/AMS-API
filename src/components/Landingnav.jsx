import React from 'react';

const LandingNav = ()=>{
    return(
        <div id="landingnav">
            <div className="nav-wrapper nav-wrap">
                <div className="logo">
                    <a className="brand-logo " href="http://localhost:3000">
                        <span className="logo-placeholder">LOGO</span>
                    </a>
                </div>
                    <ul className='right hide-on-med-and-down' style={{margin: '1rem', width: '100%', display: 'flex', justifyContent: 'flex-end'}}>
                        <li><button className="btn button-color" href="#">SIGN UP</button></li>
                    </ul>
            </div>
        </div>
    );
};

export default LandingNav;