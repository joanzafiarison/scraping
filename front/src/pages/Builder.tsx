import React , {useState} from 'react';
import Sitemap from '../components/Builder/Sitemap.tsx';
import Category from '../components/Builder/Category.tsx';


function Switcher({name}){
  switch(name){
    case "category" :
      return <Category />
    case "sitemap" :
      return <Sitemap />
    default :
      return <p>Loading</p>
  }
}
function Builder() {
  const [overlay, setOverlay] = useState("");

  return (
    <div style={{position :"relative"}}>
      <h2 className="subtitle">Build Sitemaps/ Or Entities</h2>
      <div>
        <button onClick={() => setOverlay("sitemap")}>+</button>
        <p>ajouter sitemap</p>
      </div>
      <div>
        <button onClick={() => setOverlay("category")}>+</button>
        <p>ajouter category</p>
      </div> 
      <div style={{display : overlay !== "" ? "block" : "none", position :"absolute", backgroundColor:"black", minHeight : "50vh", width:"30vw" , top: "25%", left:"20%"}}>
            <Switcher name={overlay} />
        <button onClick={() => setOverlay('')}>Fermer</button>
      </div>
    </div>
  )
}

export default Builder