import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { About } from './Components/About';
import { Users } from './Components/Users';
import { Navbar } from './Components/Navbar';

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/about" element={<About />} />
        <Route path="/" element={<Users />} />
      </Routes>
    </Router>
  );
}

export default App;
