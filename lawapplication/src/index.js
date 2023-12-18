import React from 'react';
import { createRoot } from 'react-dom/client';
import App from './App'; // Replace with the actual path to your main component

// Use createRoot instead of ReactDOM.render
const root = createRoot(document.getElementById('root'));

// Render your app component
root.render(<App />);