import React from 'react'
import { Link } from 'react-router-dom'

function Header() {
  return (
    <header>
        <h1 style={{fontSize :14, color : "black"}}><Link to="/">Scraping Hub</Link></h1>
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
                    <li style={{fontSize : 10, margin:"0.5rem"}}><Link to="/profile">Paramètres</Link></li>
                    <li style={{fontSize : 10, margin:"0.5rem"}}><Link to="/operations">Opérations</Link></li>
                    <li style={{fontSize : 10, margin:"0.5rem"}}><Link to="/search">Recherche</Link></li>
                    <li style={{fontSize : 10, margin:"0.5rem"}}><Link to="/builder">Builder</Link></li>
                </ul>
            </nav>
        </div>
      </header>
  )
}

export default Header