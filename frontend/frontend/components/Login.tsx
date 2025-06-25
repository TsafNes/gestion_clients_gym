// src/components/Login.tsx
import React, { useState } from 'react';
import axios from './axiosConfig';

const Login: React.FC = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/auth/token/', {
        username,
        password
      });
      localStorage.setItem('access', response.data.access);
      localStorage.setItem('refresh', response.data.refresh);
      alert("Connexion réussie !");
    } catch (err) {
      setError("Échec de la connexion. Vérifie tes identifiants.");
    }
  };

  return (
    <div>
      <h2>Connexion</h2>
      <form onSubmit={handleLogin}>
        <input
          type="text"
          placeholder="Nom d'utilisateur"
          value={username}
          onChange={e => setUsername(e.target.value)}
        />
        <br />
        <input
          type="password"
          placeholder="Mot de passe"
          value={password}
          onChange={e => setPassword(e.target.value)}
        />
        <br />
        <button type="submit">Se connecter</button>
      </form>
      {error && <p style={{color: 'red'}}>{error}</p>}
    </div>
  );
};

export default Login;
