import React from 'react';


function Graph({graph}) {
  return (
    <div style={{backgroundColor:"#95CFD9",  borderRadius : 10, padding :10}}>
        <div style={{display :"flex"}}>
            <div style={{display : "flex"}}>
                <p>Sites</p>
                <p>Type</p>
            </div>
            <div>
                <p>Semaine</p>
            </div>
        </div>
        <p>{graph.week.join(" ")}</p>
        
    </div>
  )
}

export default Graph