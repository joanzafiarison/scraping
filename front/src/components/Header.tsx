import React from 'react';
import { Link } from 'react-router-dom'

function Header() {
  return (
    <header>
        <Link to="/"><h1 className="logo_title">Scraping Hub</h1></Link>
        <div>
            <div style={{display :"flex", justifyContent:"center", margin:"2rem"}}>
                <Link to="/profile">
                    <figure style={{width : 50, height :50, borderRadius : "100%", backgroundColor : "grey", margin :0}}>

                    </figure>
                    <p style={{fontSize : 10, color:"black", margin:2}}>Some Dude</p>
                </Link>
            </div>
            

            <nav style={{display :"flex", alignItems: "center", margin :"0.5rem"}}>
                <ul style={{margin :0}}>
                    <Link to="/profile">
                        <li className="nav_title">Paramètres</li>
                    </Link>
                    <Link to="/operations">
                        <li className="nav_title">Opérations</li>
                    </Link>
                    <Link to="/search">
                        <li className="nav_title">Recherche</li>
                    </Link>
                    <Link to="/builder">
                        <li className="nav_title">Builder</li>
                    </Link>
                </ul>
            </nav>
        </div>
      </header>
  )
}

export default Header