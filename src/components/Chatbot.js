// src/components/Chatbot.js
import React, { useState } from 'react';
import axios from 'axios';
import './Chatbot.css';

const API_URL = 'https://tarea-3-trekash.onrender.com';  // Cambia a la URL de tu API

function Chatbot() {
    const [messages, setMessages] = useState([]);  // Almacena el historial de mensajes
    const [input, setInput] = useState('');  // Almacena el mensaje del usuario
    const [isLoading, setIsLoading] = useState(false);  // Estado para mostrar el mensaje de carga

    const sendMessage = async () => {
        if (!input.trim()) return;

        // Añadir el mensaje del usuario al historial
        setMessages([...messages, { text: input, sender: 'user' }]);
        
        // Establecer isLoading a true para mostrar el mensaje de carga
        setIsLoading(true);

        try {
            // Solicitud a la API con el mensaje del usuario
            const response = await axios.post(`${API_URL}/api/chatbot`, { query: input });
            setMessages((prevMessages) => [
                ...prevMessages,
                { text: response.data.answer, sender: 'bot' }
            ]);
        } catch (error) {
            console.error("Error al obtener la respuesta:", error);
            setMessages((prevMessages) => [
                ...prevMessages,
                { text: "Error al obtener respuesta", sender: 'bot' }
            ]);
        }
        
        // Establecer isLoading a false después de recibir la respuesta
        setIsLoading(false);
        setInput('');  // Limpiar el campo de entrada
    };

    const handleInputChange = (e) => {
        setInput(e.target.value);
    };

    const handleKeyPress = (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    };

    return (
        <div className="chatbot">
            <div className="chatbot-messages">
                {messages.map((msg, index) => (
                    <div key={index} className={`message ${msg.sender}`}>
                        <span>{msg.text}</span>
                    </div>
                ))}
                {/* Mostrar el mensaje de carga si isLoading es true */}
                {isLoading && (
                    <div className="message bot">
                        <span>Cargando respuesta...toma 1 a 2 minutos</span>
                    </div>
                )}
            </div>
            <input
                type="text"
                value={input}
                onChange={handleInputChange}
                onKeyPress={handleKeyPress}
                placeholder="Escribe tu mensaje..."
                disabled={isLoading}  // Deshabilitar el input mientras se espera la respuesta
            />
            <button onClick={sendMessage} disabled={isLoading}>Enviar</button>
        </div>
    );
}

export default Chatbot;