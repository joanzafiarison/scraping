import React ,  {useState, useEffect} from 'react'

function ErrorPanel({errors}) {
    const [expand, setExpand] = useState(false)
    const [visibleErrors, setVisibleErrors] = useState(errors.slice(0,1));

    useEffect(() => {
        if(expand){
            setVisibleErrors(errors)
        }
        else{
            setVisibleErrors(errors.slice(0,1))
        }
    },[expand])
  return (
    <div>
        <h2>Errors</h2>
        <div style={{width: "100%", border : "2px solid black"}}></div>
        <ul>
            {visibleErrors.map((err,k) => (
                <li style={{display : "flex", justifyContent : "space-around"}}>
                    <p>{err.time}</p>
                    <p style={{color : "red"}}>Desc : {err.desc}</p>
                </li>
            ))}
        </ul>
        <button onClick={() => setExpand(!expand)}>Expand</button>
    </div>
  )
}

export default ErrorPanel