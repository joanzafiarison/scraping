import { useState } from 'react';
import { Routes, Route } from 'react-router-dom';
import Home from "./pages/Home";
import Search from './pages/Search';
import Profile from "./pages/Profil";
import Builder from './pages/Builder';
import Operations from './pages/Operations';
import Login from './pages/Login';

import Header from "./components/Header";

import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div style={{display : "flex"}}>
      <Header />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/search" element={<Search />} />
        <Route path="/profile" element={<Profile/>} />
        <Route path="/login" element={<Login />} />
        <Route path="/operations" element={<Operations />} />
        <Route path="/builder" element={<Builder />} />
      </Routes>
    </div>
  )
}

export default App
