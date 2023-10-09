import React , {useState, useEffect, useRef, Component} from 'react';
import * as d3 from "d3";


type GraphData = {
  graph : {
    week : string[],
    month : string[]
  }

}

function Graph({graph}  : GraphData) {
  const [timeline, setTimeline ] =useState("month");
  const [type, setType] = useState("lang")

  const svgRef = useRef(null);
  
  useEffect(()=> {
    console.log("effect", graph[timeline])

    if(timeline && svgRef.current ){
      const svg = d3.select(svgRef.current);
      
      
      //bind d3 data
      const update =  svg.selectAll("rect")
                          .append("g")
                          .data(graph[timeline])

    
      //Display D3 data
      update.enter()
            .append('text')
            .attr('x', (d, i) => i * 50)
            .attr('y', 250)
            .style('font-size', 24)
            .text((d: number) => d);
      
      //make bars     
      update.enter()
            .append("rect")
            .attr("x", (d, i) => i * 50)
            .attr("y", (d, i) => 200 - 5 *d)
            .attr("width", 45)
            .attr("height", (d, i) => d * 5)
            .attr("fill", "green")

      //remove
      update.exit()
            .remove()
      
      
    }
    
    //drawChart(data[timeline])
  },[timeline, svgRef.current])

  return (
    <div style={{backgroundColor:"#95CFD9",  borderRadius : 10, padding :10, minWidth : "10rem"}}>
        <div style={{display :"flex"}}>
            <div style={{display : "flex"}}>
                <p>Sites</p>
                <select onChange={(e) => setType(e.target.value)}>
                  <option value="Langue">Langue</option>
                  <option value="Immo">Immobilier</option>
                </select>
            </div>
            <div style={{display : "flex"}}>
                <p>{timeline}</p>
                <select onChange={(e) =>setTimeline(e.target.value)}>
                  <option value="week">Week</option>
                  <option value="month">Month</option>
                </select>
            </div>
        </div>
        <svg 
            id="graph"
            width={300}
            height={300}
            ref={svgRef}
        />
        
    </div>
  )
}

export default Graph