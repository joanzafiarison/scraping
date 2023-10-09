import React from 'react'

function Profil() {
  return (
    <div>
      <div style={{display :"flex"}}>
          <div className="box" style={{backgroundColor : "#DABAA3"}}>
              <h2>Générales</h2>
              <form>
                <p>Email<input type="text" name="" id="" /></p>
                <p>Pseudo<input type="text" name="" id="" /></p>
                <p>Mot de passe<input type="text" name="" id="" /></p>
                <input type="submit" value="Modifier" />
              </form>
          </div>
          <div className="box" style={{backgroundColor : "#A74C62"}}>
              <h2>Paiement</h2>
          </div>
      </div>
      <div className="box" style={{backgroundColor : "#628993"}}>
            <h2>FAQ</h2>
      </div>
    </div>
  )
}

export default Profil