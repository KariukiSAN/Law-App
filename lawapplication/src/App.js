import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HeaderFooter from './HeaderFooter';

const Home = () => <div>Home Content</div>;
const Services = () => <div>Services Content</div>;
const Appointment = () => <div>Appointment Content</div>;
const Feedback = () => <div>Feedback Content</div>;
const PrivacyPolicy = () => <div>Privacy Policy Content</div>;
const Contact = () => <div>Contact Content</div>;

const App = () => {
  return (
    <Router>
      <div>
        <HeaderFooter />

        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/services" element={<Services />} />
          <Route path="/appointment" element={<Appointment />} />
          <Route path="/feedback" element={<Feedback />} />
          <Route path="/privacy-policy" element={<PrivacyPolicy />} />
          <Route path="/contact" element={<Contact />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;