import React , {Component} from 'react';


type GraphData = {
  graph : {
    week : string[],
    month : string[]
  }

}

function Graph({graph}  : GraphData) {
  return (
    <div style={{backgroundColor:"#95CFD9",  borderRadius : 10, padding :10, minWidth : "10rem"}}>
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