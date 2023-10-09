import React from 'react'


type ResultItem = {
  result : {
    m1 : number,
    m2 : number,
    found : number,
    passed : number
  }
}

function ResultCard( { result } : ResultItem ) {
  return (
    <div style={{backgroundColor:"#8D7373",  borderRadius : 10, padding :10, minWidth : "12rem", color : "black"}}>
        <p className="subtitle">Collection X</p>
        <div style={{display :"flex", justifyContent : "space-around", margin :"1.5rem"}}>
            <div>
              <p className="metric">{result.m1}%</p>
              <p className="metric_detail">accuracy</p>
            </div>
            <div>
              <p className="metric">{result.m2}%</p>
              <p className="metric_detail">recognition</p>
            </div>
        </div>
        <p>Item Found {result.found}</p>
        <p>Test passed {result.passed}</p>
        <button style={{ border : "none", borderRadius : 10, boxShadow : "1px 1px 3px grey"}}><p style={{margin : 0, fontSize :10, fontWeight : 200}}>Modifier</p></button>
    </div>
  )
}

export default ResultCard