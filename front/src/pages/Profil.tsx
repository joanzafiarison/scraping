import React from 'react'

function Profil() {
  return (
    <div>
      <div style={{display :"flex"}}>
          <div className="box" style={{backgroundColor : "#DABAA3",margin :"1rem", padding:"2rem"}}>
              <h2 className="subtitle">Générales</h2>
              <form>
                <p>Email<input type="text" name="" id="" /></p>
                <p>Pseudo<input type="text" name="" id="" /></p>
                <p>Mot de passe<input type="text" name="" id="" /></p>
                <button className="secondary">Modifier</button>
              </form>
          </div>
          <div className="box" style={{backgroundColor : "#A74C62", minWidth:"10rem", margin :"1rem"}}>
              <h2 className="subtitle">Paiement</h2>
          </div>
      </div>
      <div className="box" style={{backgroundColor : "#628993", minHeight:"6rem", margin :"1rem"}}>
            <h2 className="subtitle">FAQ</h2>
      </div>
    </div>
  )
}

export default Profil