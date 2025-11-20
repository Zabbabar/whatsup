import logo from './logo.svg';
import './App.css';
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';


function App() {
  const [reviews, setReviews] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/reviews')
      .then(response => setReviews(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div className="App">
      <h1>Product Reviews</h1>
      <table>
        <thead>
          <tr>
            <th>User Name</th>
            <th>Product</th>
            <th>Review</th>
            <th>Timestamp</th>
          </tr>
        </thead>
        <tbody>
          {reviews.map(review => (
            <tr key={review.id}>
              <td>{review.user_name}</td>
              <td>{review.product_name}</td>
              <td>{review.product_review}</td>
              <td>{new Date(review.created_at).toLocaleString()}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
