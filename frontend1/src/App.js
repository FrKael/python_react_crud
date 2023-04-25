import React from "react";
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import { Users } from './components/Users';
import { About } from './components/About';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/About" element={<About />} />
        <Route path="/" element={<Users />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;