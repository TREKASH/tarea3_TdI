// src/App.js
import React from 'react';
import Chatbot from './components/Chatbot';
import Photos from './components/Photos';
import './App.css';

function App() {
    return (
        <div className="App">
            <h1>Chatbot</h1>
            <Chatbot />
            <h1>Peliculas disponibles para chatear</h1>
            <Photos />
        </div>
    );
}

export default App;