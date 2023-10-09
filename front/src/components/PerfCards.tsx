import React from 'react'

function PerfCards({perf}) {
  return (
    <div style={{backgroundColor: "#DABAA3", borderRadius : 10, padding :10}}>
        <div style={{display : "flex", justifyContent : "space-around"}}>
            <div style={{width : "20%"}}>
                <p>Performance</p>
                <p style={{fontSize :10}}>Différentes mesures à surveiller</p>
            </div>
            <div style={{display :"flex", justifyContent:"space-around"}}>
                <div style={{backgroundColor : "white", color :"black", borderRadius : 10, padding : 2, minWidth :"5rem"}}>
                    <p>Url parsed</p>
                    <p>{perf.url}</p>
                </div>
                <div style={{backgroundColor : "white", color :"black", borderRadius : 10, padding : 2 , minWidth :"5rem"}}>
                    <p>Success</p>
                    <p>{perf.success}%</p>
                </div>
                <div style={{backgroundColor : "white", color :"black", borderRadius : 10, padding : 2, minWidth :"5rem"}}>
                    <p>Metric</p>
                    <p>{perf.metric}</p>
                </div>
            </div>
        </div>
  </div>
  )
}

export default PerfCards