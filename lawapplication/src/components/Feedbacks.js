import React, { useState, useEffect } from 'react';
import './feedback.css';
import p from './images/p.jpg';
import p1 from './images/p1.jpg';
import p2 from './images/p2.jpg';
import p3 from './images/p3.jpg';
import p4 from './images/p4.jpg';

const Feedbacks = () => {
  const [feedbacks, setFeedbacks] = useState([]);
  
  const [newFeedback, setNewFeedback] = useState('');

  useEffect(() => {
    const fetchFeedbacks = async () => {
      try {
        const response = await fetch('http://127.0.0.1:5000/feedbacks');
        if (!response.ok) {
          throw new Error(`Error fetching feedbacks: ${response.status} ${response.statusText}`);
        }
        const data = await response.json();
        console.log('Fetched Feedbacks:', data); // Log the entire data object to the console
        setFeedbacks(data);
      } catch (error) {
        console.error(error.message);
      }
    };

    fetchFeedbacks();
  }, []);

  const handleAddFeedback = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/feedbacks', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: newFeedback }),
      });

      if (!response.ok) {
        throw new Error(`Error adding feedback: ${response.status} ${response.statusText}`);
      }

      const data = await response.json();
      setFeedbacks([...feedbacks, data]);
      setNewFeedback('');
    } catch (error) {
      console.error(error.message);
    }
  };

  const handleDelete = async (feedbackId) => {
    try {
      const response = await fetch(`http://127.0.0.1:5000/feedbacks/${feedbackId}`, {
        method: 'DELETE',
      });

      if (!response.ok) {
        throw new Error(`Error deleting feedback: ${response.status} ${response.statusText}`);
      }

      const updatedFeedbacks = feedbacks.filter((feedback) => feedback.id !== feedbackId);

      setFeedbacks(updatedFeedbacks);
    } catch (error) {
      console.error(error.message);
    }
  };

  const handleLike = async (feedbackId) => {
    try {
      const response = await fetch(`http://127.0.0.1:5000/feedbacks/${feedbackId}/like`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (!response.ok) {
        throw new Error(`Error liking feedback: ${response.status} ${response.statusText}`);
      }

      const updatedFeedbacks = feedbacks.map((feedback) =>
        feedback.id === feedbackId ? { ...feedback, likes: feedback.likes + 1 } : feedback
      );

      setFeedbacks(updatedFeedbacks);
    } catch (error) {
      console.error(error.message);
    }
  };

  return (
    <div className='feedback-page'>
      <div className="feedback-container">
        <h1>Feedback</h1>
        {feedbacks.map((feedback, index) => (
          <div key={feedback.id} className="feedback-item">
            {index < 5 && (
              <img
                src={
                  index === 0 ? p : index === 1 ? p1 : index === 2 ? p2 : index === 3 ? p3 : p4
                }
                alt="person"
                className="person-img"
              />
            )}
            <div className="feedback-text">{feedback.text}</div>
            <div className='button-container'>
              <div className="feedback-buttons">
                <button onClick={() => handleLike(feedback.id)} className="like-button">❤️</button>
                <button onClick={() => handleDelete(feedback.id)} className="delete-button">🗑️</button>
              </div>
            </div>
          </div>
        ))}
      </div>
      <div className='leavefeedback'>
        <h3>Leave a Feedback:</h3>
        <input
          type="text"
          value={newFeedback}
          onChange={(e) => setNewFeedback(e.target.value)}
        />
        <button onClick={handleAddFeedback}>Submit Feedback</button>
      </div>
    </div>
  );
};

export default Feedbacks;

