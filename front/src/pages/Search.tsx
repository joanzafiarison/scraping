import React from 'react'

function Search() {
  return (
    <div className="main_container">
      <form action="">
        <p><input type="text" name="search" id="search" placeholder='search item name, ref, category' /></p>
      </form>
      <div>
        <ul style={{display:"flex"}}>
          {["marque", "reference", "produit", "categorie"].map(el =>(
            <li className="filter">
              <div className="square"></div>
              <p>{el}</p>
            </li>
          ))}
        </ul>
      </div>
      <div className="box" style={{backgroundColor :"#DABAA3"}}>
        <div>
          {[{"name": "Acer XE456"},{"name": "IMac"},{"name": "BledAir"}].map((prd) => (
            <div className="product_line">
              <p style={{margin:5}}>{prd.name}</p>
              <button>Details</button>
              <p style={{margin:5}}>X times</p>
            </div>
          ))}
        </div>
        <button style={{alignSelf:"flex-end", margin:"1rem"}}>Exporter</button>
      </div>
    </div>
  )
}

export default Search