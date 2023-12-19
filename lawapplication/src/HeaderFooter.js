// HeaderFooter.js

import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import './HeaderFooter.css';

const HeaderFooter = () => {
  const [headerBackground, setHeaderBackground] = useState(0);
  const [showSignUpForm, setShowSignUpForm] = useState(false);
  const [showLoginForm, setShowLoginForm] = useState(false);

  useEffect(() => {
    const interval = setInterval(() => {
      setHeaderBackground(prevBackground => (prevBackground + 1) % 3);
    }, 10000);

    return () => clearInterval(interval);
  }, []);

  const headerImages = [
    '/images/55e5d2444857a814ea898675c6203f78083edbe352577140702b7e_1280_legal.jpg',
    '/images/decreto-penale-di-condanna.jpg',
    '/images/202204_12-Differences-entre-un-avocat-daffaires-et-un-juriste-dentreprise.jpg',
  ];

  const handleSignUpClick = () => {
    setShowSignUpForm(true);
    setShowLoginForm(false);
  };

  const handleLoginClick = () => {
    setShowLoginForm(true);
    setShowSignUpForm(false);
  };

  return (
    <div>
      {/* Header Section */}
      <header style={{ backgroundImage: `url(${headerImages[headerBackground]})` }}>
        <div>
          <img src="/images/4571f45c45a8ba0367b38cba8b889f2f.jpg" alt="Firm Logo" />
        </div>
        <nav>
          <ul>
            <li><Link to="/">About Us</Link></li>
            <li><Link to="/services">Our Services</Link></li>
            <li><Link to="/appointment">Book an Appointment</Link></li>
            <li><Link to="/feedback">Feedback</Link></li>
          </ul>
        </nav>
        <div>
          <button onClick={handleLoginClick}>Login</button>
          <button onClick={handleSignUpClick}>Sign Up</button>
        </div>
      </header>

      {showLoginForm && (
        <div>
          <h2>Welcome Back!</h2>
          <form>
            <label htmlFor="usernameOrEmail">Username, Phone Number, or Email:</label>
            <input type="text" id="usernameOrEmail" placeholder="Enter your username, phone number, or email" />

            <label htmlFor="password">Password:</label>
            <input type="password" id="password" placeholder="Enter your password" />

            <p><Link to="/forgot-password">Forgot password?</Link></p>

            <button type="submit">Sign In</button>
          </form>
        </div>
      )}

      {showSignUpForm && (
        <div>
          <h2>Hello, We are glad to have you here. Welcome to our community!</h2>
          <form>
            <label htmlFor="fullName">Full Name:</label>
            <input type="text" id="fullName" placeholder="Enter your full name" />

            <label htmlFor="username">Username:</label>
            <input type="text" id="username" placeholder="Enter your username" />

            <label htmlFor="phoneNumber">Phone Number:</label>
            <input type="text" id="phoneNumber" placeholder="Enter your phone number" />

            <label htmlFor="email">Email Address:</label>
            <input type="email" id="email" placeholder="Enter your email address" />

            <label htmlFor="password">Set up Preferred Password:</label>
            <input type="password" id="password" placeholder="Enter your preferred password" />

            <label htmlFor="confirmPassword">Confirm Password:</label>
            <input type="password" id="confirmPassword" placeholder="Confirm your password" />

            <button type="submit">Sign Up</button>
          </form>
        </div>
      )}

      {/* Footer Section */}
      <footer style={{ backgroundImage: 'url(/images/istockphoto-1251143642-612x612.jpg)' }}>
        <div className="footer-content">
          <div>
            <h3>Quick Links</h3>
            <ul>
              <li><Link to="/">About Us</Link></li>
              <li><Link to="/services">Our Services</Link></li>
              <li><Link to="/blogs">Blogs</Link></li>
            </ul>
          </div>
          <div>
            <h3>Privacy Policy</h3>
            <Link to="/privacy-policy">Privacy Policy</Link>
          </div>
          <div>
            <h3>Contact Info</h3>
            <p>Email: law@sheria.com</p>
            <p>Phone: +2547123456789</p>
          </div>
          <div>
            <h3>Our Social Media</h3>
            <a href="https://facebook.com" target="_blank" rel="noopener noreferrer">Facebook</a>
            <a href="https://twitter.com" target="_blank" rel="noopener noreferrer">Twitter</a>
            <a href="https://linkedin.com" target="_blank" rel="noopener noreferrer">LinkedIn</a>
          </div>
          <div>
            <h3>Get in Touch</h3>
            <input type="email" placeholder="Enter your email" />
            <button>Subscribe</button>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default HeaderFooter;