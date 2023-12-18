import React, { useState } from 'react';  // Combine the imports

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css';
import Home from './components/Home';
import Signup from './components/Signup';
import Login from './components/Login';
import Dashboard from './components/Dashboard';
import Feedbacks from './components/Feedbacks';

function App() {
  const [service, setService] = useState('service1');
  const [date, setDate] = useState('');
  const [time, setTime] = useState('');
  const [successMessage, setSuccessMessage] = useState('');

  const bookAppointment = (e) => {
    e.preventDefault();
    
    // Perform the booking logic here
    // For demonstration purposes, let's assume the booking was successful
    setSuccessMessage('Appointment booked successfully!');
    setTimeout(() => {
      setSuccessMessage('');
    }, 5000); // Hide the success message after 5 seconds
  };

  return (
    <div>
      <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/login" element={<Login />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/feedbacks" element={<Feedbacks />} />
        </Routes>
      </Router>

      <h1>Law-App!</h1>

      <div className="card">
        <h2>Book Services/Appointment</h2>
        <form onSubmit={bookAppointment}>
          <label htmlFor="service">Select Service:</label>
          <select id="service" name="service" value={service} onChange={(e) => setService(e.target.value)}>
            <option value="service1">Service 1</option>
            <option value="service2">Service 2</option>
            <option value="service3">Service 3</option>
          </select>

          <label htmlFor="date">Select Date:</label>
          <input type="date" id="date" name="date" required value={date} onChange={(e) => setDate(e.target.value)} />

          <label htmlFor="time">Select Time:</label>
          <input type="time" id="time" name="time" required value={time} onChange={(e) => setTime(e.target.value)} />

          <button type="submit">Book Now</button>
        </form>
      </div>

      {successMessage && (
        <div className="success-message">{successMessage}</div>
      )}
    </div>
  );
}

export default App;
