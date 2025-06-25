import React, { useState } from 'react';
import axios from './axiosConfig';

const RegisterClient: React.FC = () => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');

  const handleRegister = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const res = await axios.post('/auth/register/', {
        username,
        email,
        password
      });
      setMessage("Compte créé avec succès !");
    } catch (err) {
      setMessage("Erreur lors de l'inscription.");
    }
  };

  return (
    <div>
      <h2>Inscription</h2>
      <form onSubmit={handleRegister}>
        <input
          type="text"
          placeholder="Nom d'utilisateur"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />
        <br />
        <input
          type="email"
          placeholder="Courriel"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <br />
        <input
          type="password"
          placeholder="Mot de passe"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <br />
        <button type="submit">S'inscrire</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
};

export default RegisterClient;
