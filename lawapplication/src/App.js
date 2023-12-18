
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import Home from './components/Home';
import Signup from './components/Signup';
import Login from './components/Login';
import Dashboard from './components/Dashboard';
import Feedbacks from './components/Feedbacks';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/login" element={<Login />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/feedbacks" element={<Feedbacks />} />
      </Routes>
    </Router>
  );
}

export default App;
