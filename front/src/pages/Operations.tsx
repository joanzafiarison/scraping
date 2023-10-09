import React from 'react'

function Operations() {
  return (
    <div style={{backgroundColor : "#D8D6D4"}}>
        <div>
            <h2 className="subtitle">Planification</h2>
            <div>Frise</div>
            <ul style={{display :"flex"}}>
                {[5,8,12, 14, 16, 18, 22, 0].map(el =>(
                    <li>{el}h</li>
                ))}
            </ul>
            <button>Liste</button>
            <button>Ajouter</button>
        </div>
        <div className="box" style={{backgroundColor :"#DABAA3"}}>
            <h2 className="subtitle"> Test Personnalisé</h2>
            <div style={{display : "flex"}}>
                <form>
                    <p>Url <input type="text" name="url" id="url" /></p>
                    <p>choix sitemap</p>
                    <select>
                        <option value ="A">A</option>
                    </select>
                </form>
                <div style={{backgroundColor :"black", color :"green", width :200, height : 200}}>

                </div>
                
            </div>
            <button>Extraire</button>
            
        </div>
    </div>
  )
}

export default Operations