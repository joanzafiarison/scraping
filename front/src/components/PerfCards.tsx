import React from 'react'


type PerfItem = {
    performance : {
        url : number,
        success : number,
        metric : number
    }
}
function PerfCards({performance} : PerfItem) {
  return (
    <div style={{display : "flex", flexDirection:"column", justifyContent : "center", minHeight :"10rem", backgroundColor: "#DABAA3", borderRadius : 10, padding :10}}>
        <div style={{display : "flex", justifyContent : "space-around"}}>
            <div style={{width : "20%"}}>
                <p>Performance</p>
                <p style={{fontSize :10}}>Différentes mesures à surveiller</p>
            </div>
            <div style={{display :"flex", justifyContent:"space-around"}}>
                <div style={{backgroundColor : "white", color :"black", borderRadius : 10, padding : 2, minWidth :"5rem", margin : 10}}>
                    <p>Url parsed</p>
                    <p>{performance.url}</p>
                </div>
                <div style={{backgroundColor : "white", color :"black", borderRadius : 10, padding : 2 , minWidth :"5rem", margin : 10}}>
                    <p>Success</p>
                    <p>{performance.success}%</p>
                </div>
                <div style={{backgroundColor : "white", color :"black", borderRadius : 10, padding : 2, minWidth :"5rem", margin : 10}}>
                    <p>Metric</p>
                    <p>{performance.metric}</p>
                </div>
            </div>
        </div>
  </div>
  )
}

export default PerfCards