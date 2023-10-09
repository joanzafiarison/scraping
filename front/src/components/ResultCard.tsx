import React from 'react'

function ResultCard({result}) {
  return (
    <div style={{backgroundColor:"#8D7373",  borderRadius : 10, padding :10, color : "black"}}>
        <p>Collection X</p>
        <div style={{display :"flex", justifyContent : "center"}}>
            <p>{result.m1}%</p>
            <p>{result.m2}%</p>
        </div>
        <p>Item Found {result.found}</p>
        <p>Test passed {result.passed}</p>
        <button style={{ border : "none", borderRadius : 10, boxShadow : "1px 1px 3px grey"}}><p style={{margin : 0, fontSize :10, fontWeight : 200}}>Modifier</p></button>
    </div>
  )
}

export default ResultCard