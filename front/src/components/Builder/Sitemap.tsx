import React , {useState} from 'react';
import axios from "axios";

const MOCK_CATEGORY = ["immo","dictionnary"];

function Sitemap() {
    const [meta, setMeta] = useState({});
    function handleSubmit (e) {
        e.preventDefault();
        axios.post("http://localhost:5000/sitemap", meta)
          .then(res=> console.log(res))
          .catch(err=> console.log(err))
    }

  return (
    <div>
        <h2>Accueil</h2>
        <form onSubmit={handleSubmit}>
            <p style={{color:"grey"}}>Nom: <input type="text" name="name" onChange={(e) => setMeta({...meta,name : e.target.value})}/></p>
            <p style={{color:"grey"}}>Plural : <input type="text" name="plural" onChange={(e) => setMeta({...meta,plural : e.target.value})}/></p>
            <p style={{color:"grey"}}>URL : <input type="text" name="url" onChange={(e) => setMeta({...meta,main_url : e.target.value})}/></p>
            <p style={{color:"grey"}}>Card : <input type="text" name="card" onChange={(e) => setMeta({...meta,card : e.target.value})}/></p>
            <p style={{color:"grey"}}>Link : <input type="text" name="link" onChange={(e) => setMeta({...meta,link : e.target.value})}/></p>
            <p style={{color:"grey"}}>Search Bar : <input type="text" name="link" onChange={(e) => setMeta({...meta,searchbar : e.target.value})}/></p>
            <p style={{color:"grey"}}>Search Button : <input type="text" name="link" onChange={(e) => setMeta({...meta,search_button : e.target.value})}/></p>
            <p style={{color:"grey"}}>Category : 
              <select onChange={(e) => setMeta({...meta, category : e.target.value})}>
                {MOCK_CATEGORY.map((el, k) => (
                  <option key={k} value={el}>{el}</option>
                ))}
              </select>
            </p>
            <button onClick={() => setMeta({})}>Réinitialiser</button>
            <input type="submit" value="Valider" />
        </form>
    </div>
  )
}

export default Sitemap