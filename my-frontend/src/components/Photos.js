// src/components/Photos.js
import React from 'react';
import './Photos.css';

const Photos = () => {
  return (
    <div className="photosfilm">
      {[...Array(10)].map((_, index) => (
        <img
          key={index}
          src={`${process.env.PUBLIC_URL}photo${index + 1}.jpg`}
          alt={`photo ${index + 1}`}
          className="grid-image"
        />
      ))}
    </div>
  );
};

export default Photos;