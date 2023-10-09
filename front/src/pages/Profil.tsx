import React from 'react'

function Profil() {
  return (
    <div>
      <div style={{display :"flex"}}>
          <div className="box" style={{backgroundColor : "#DABAA3"}}>
              <h2 className="subtitle">Générales</h2>
              <form>
                <p>Email<input type="text" name="" id="" /></p>
                <p>Pseudo<input type="text" name="" id="" /></p>
                <p>Mot de passe<input type="text" name="" id="" /></p>
                <button className="secondary">Modifier</button>
              </form>
          </div>
          <div className="box" style={{backgroundColor : "#A74C62"}}>
              <h2 className="subtitle">Paiement</h2>
          </div>
      </div>
      <div className="box" style={{backgroundColor : "#628993"}}>
            <h2 className="subtitle">FAQ</h2>
      </div>
    </div>
  )
}

export default Profil