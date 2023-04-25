import React from 'react';
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import { About } from './Components/About';
import { Users } from './Components/Users';
import { Navbar } from './Components/Navbar';


function App() {
  return (
    <Router>
      <Navbar/>
      <div className='container p-4'>
        <Routes>
          <Route path="/About" component={About}/>
          <Route path="/" component={Users}/>
        </Routes>
      </div>
    </Router>

  );
}

export default App;
