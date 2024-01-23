import React , { useState, useEffect } from 'react';
import axios from "axios";
import ErrorPanel from '@/components/Panels/ErrorPanel';
import ScreenPanel from '@/components/Panels/ScreenPanel';

function Operations() {
    const [isCustom, setCustom] = useState("existing");
    const [url, setUrl] = useState("");
    const [sitemaps, setSitemaps] = useState(["A","B"]);
    const [chosenSitemap, setChosenSitemap] = useState("")
    const [models, setModels] = useState(["A","B","C"]);
    const [chosenModel, setChosenModel] = useState("")
    const [errors, setErrors] = useState(["erreur1","erreur 3"])
    const [result, setResult] = useState({}) // html, processed
    const [overlay, setOverlay] = useState('')
    
    const SERVER_URL = "http://localhost"
    useEffect(() => {
        axios.get(`${SERVER_URL}/models`)
            .then((res) => {
                setModels(res.data)
            })
            .catch((err) => console.log(err))
        
        axios.get(`${SERVER_URL}/sitemaps`)
            .then((res) => {
                setSitemaps(res.data)
            })
            .catch((err) => console.log(err))
        //loadModels //loadSitemap
    },[])
    const onOptionChange = (e) => {
        setCustom(e.target.value);
        //extract endpoint  .. url, model, sitemap
    }
    const onSubmit = (e) => {
        e.preventDefault();
        let data = {
            url : url,
            sitemap : chosenSitemap,
            model : chosenModel
        }
        axios.post(`${SERVER_URL}/operation`, data )
            .then( (res) => {
                setResult(res.data);
            })
            .catch( (err) => {
                console.log(err)
            })

    }
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
            <div style={{display : "flex", flexDirection:"column"}}>
                <form onSubmit={onSubmit}>
                    <p>Url  : <input type="text" name="url" id="url" /></p>
                    <div>
                        <input 
                            type="radio" 
                            name="sitemapExist" 
                            value="existing" 
                            id="existing" 
                            checked={isCustom === "existing"}
                            onChange={onOptionChange}
                        />
                        <label htmlFor="regular">Existant</label>
                        <input 
                            type="radio" 
                            name="sitemapExist" 
                            value="custom" 
                            id="custom"
                            checked={isCustom === "custom"}
                            onChange={onOptionChange}
                        />
                        <label htmlFor="regular">Personnalisé</label>
                    </div>
                    <div style={{display:"flex"}}>
                        <p>Choisir un sitemap</p>
                        <select name="sitemaps" >
                            {sitemaps.map((el,k) => (
                                <option value={el}>{el}</option>
                            ))}
                        </select>
                    </div>
                    <div style={{display: isCustom == "custom" ?"flex" : "none" }}>
                        <p>Choisir un model</p>
                        <select name="models" >
                            {models.map((el,k) => (
                                <option value={el}>{el}</option>
                            ))}
                        </select>
                    </div>
                    <button>Extraire</button>
                </form>
                <div style={{backgroundColor :"black", color :"green", height : 200, position:"relative", margin : "1em 0em"}}>
                                <div>
                                    <ul>
                                        {errors.map((el,k) => (
                                            <li key={k}>{el}</li>
                                        ))}
                                    </ul>
                                </div>
                                <div style={{display :"flex", justifyContent:"space-around", width : "100%", backgroundColor:"brown", position:"absolute", bottom :"0%"}}>
                                    <div onClick={() => setOverlay("screenshot")}>
                                        <figure style={{width:30, height: 30, border:"1px solid black", margin:0}}>
                                            <img src="" alt="screen" />
                                        </figure>
                                    </div>
                                    <div onClick={() => setOverlay("download")}>
                                        <figure style={{width:30, height: 30,  border:"1px solid black", margin:0} }>
                                            <img src="" alt="download" />
                                        </figure>
                                    </div>
                                    <div onClick={() => setOverlay("error")}>
                                        <figure style={{width:30, height: 30, border:"1px solid black", margin:0}}>
                                            <img src="" alt="error" />
                                        </figure>
                                    </div>
                                </div>
                </div>
                <div style={{zIndex : 10, display : overlay !== "" ? "flex" : "none", flexDirection:"column", alignItems :"center",position:"absolute", width:500, height:"50vh", backgroundColor:"white", boxShadow:"1px 1px 1px grey", top:"20%"}}>
                    <p style={{color : "black"}}>{overlay}</p>
                    <button style={{height:30, width:30}} onClick={() => setOverlay("")}>X</button>
                </div>
                ,
            </div>
            
            
        </div>
    </div>
  )
}

export default Operations