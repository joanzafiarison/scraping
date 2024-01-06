import React , {useState} from 'react';
import axios from "axios";

function Category() {
    const [meta, setMeta] = useState({});
    const [keys, setKeys] = useState([]);
    const [overlay, setOverlay] = useState(false);
    const [newKey, setNewKey] = useState("");

    function handleSubmit (e) {
        e.preventDefault();
        const data = {...meta, keys : keys};
        axios.post("http://localhost:5000/category", data)
          .then(res=> console.log(res))
          .catch(err=> console.log(err))
    }

    function handleNewKey(e){
        e.preventDefault();
        if (newKey !=="") {
            let newKeys = [...keys,newKey]
            setNewKey("");
            setKeys(newKeys);
        }
        
    }

  return (
    <div>
        <h2>Catégorie</h2>
        <form onSubmit={handleSubmit}>
            <p style={{color:"grey"}}>Nom: <input type="text" name="name" onChange={(e) => setMeta({...meta,name : e.target.value})}/></p>
            {keys.map((el, k) => (
                <div style={{backgroundColor:"lightgreen", padding :5 , borderRadius :5, maxWidth : 100 , margin : 5}}>{el}</div>
            ))}
            <button onClick={() => {setMeta({}); setKeys([]);}}>Réinitialiser</button>
            <input type="submit" value="Valider" />
        </form>
        <button onClick={() => setOverlay(!overlay) }>Ajouter</button>
        <form style={{display : overlay ? "block" : "none"}} onSubmit={handleNewKey}>
            <p> Nouvelle clé : <input type="text" name="newKey"  onChange={(e) => setNewKey(e.target.value)}/></p>
            <input type="submit" value="Valider" />
        </form>
    </div>
  )
}

export default Category