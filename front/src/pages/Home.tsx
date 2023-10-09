import React , {useState, useEffect} from 'react';
import ResultCard from '../components/ResultCard';
import Graph from '../components/Graph';
import PerfCards from '../components/PerfCards';

const dash_data = {
  "result" : {
    "m1" : 75,
    "m2" : 56,
    "found" : 280,
    "passed" : 300
  },
  "graph" : {
    "week" : [4, 5, 6 , 10],
    "month" : [10, 20 , 34, 50]
  },
  "performance" : {
    "url" : 18268,
    "success" : 85,
    "metric" : 276
  }
}
function Home() {

  useEffect( () => {
    //fetch dash data
  },[])
  return (
    <div style={{padding : 10, backgroundColor:"#D8D6D4", borderRadius: 10}}>
        <div style={{display :"flex", justifyContent :"space-around"}}>
            <ResultCard result={dash_data.result}/>
            <Graph graph={dash_data.graph}/>
        </div>
        <PerfCards perf={dash_data.performance}/>
    </div>
  )
}

export default Home