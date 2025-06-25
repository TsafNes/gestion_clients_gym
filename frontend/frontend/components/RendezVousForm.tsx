import React, { useState, useEffect } from 'react';
import axios from './axiosConfig';

export default function RendezVousForm() {
  const [specialistes, setSpecialistes] = useState([]);
  const [specialiste, setSpecialiste] = useState('');
  const [date, setDate] = useState('');
  const [duree, setDuree] = useState(30);

  useEffect(() => {
    axios.get('/api/users?role=specialiste').then((res) => setSpecialistes(res.data));
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    await axios.post('/api/rendezvous/', {
      client: /* id client actuel */,
      specialiste,
      date_heure: date,
      duree,
      statut: 'prévu'
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <select value={specialiste} onChange={(e) => setSpecialiste(e.target.value)}>
        {specialistes.map((s) => (
          <option key={s.id} value={s.id}>{s.nom}</option>
        ))}
      </select>
      <input type="datetime-local" value={date} onChange={(e) => setDate(e.target.value)} />
      <input type="number" value={duree} onChange={(e) => setDuree(Number(e.target.value))} />
      <button type="submit">Prendre rendez-vous</button>
    </form>
  );
}
