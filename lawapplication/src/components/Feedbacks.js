import React, { useState, useEffect } from 'react';

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
    <div>
      <h1>Feedback</h1>
      <div>
      {feedbacks.map((feedback) => (
      <div key={feedback.id} style={{ marginBottom: '30px' }}>
       {feedback.text}
       <div>
      <button style={{ marginTop: '10px' }}onClick={() => handleLike(feedback.id)}>❤️ </button>
      <span>{feedback.likes} likes</span>
     </div>
  </div>
))}

      </div>
      <div>
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
