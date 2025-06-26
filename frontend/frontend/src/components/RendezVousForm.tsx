import React, { useState, useEffect } from 'react';
import axios from './axiosConfig';

type Specialiste = {
  id: number;
  nom: string;
};

export default function RendezVousForm() {
  const [specialistes, setSpecialistes] = useState<Specialiste[]>([]);
  const [specialiste, setSpecialiste] = useState<string>('');
  const [date, setDate] = useState<string>('');
  const [duree, setDuree] = useState<number>(30);

  useEffect(() => {
    axios.get('/api/users?role=specialiste')
      .then((res) => setSpecialistes(res.data))
      .catch((err) => console.error("Erreur lors du chargement des spécialistes :", err));
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!specialiste || !date || !duree) {
      alert("Veuillez remplir tous les champs.");
      return;
    }

    try {
      await axios.post('/api/rendezvous/', {
        client: 1, // à remplacer par l'ID du client connecté
        specialiste,
        date_heure: date,
        duree,
        statut: 'prévu'
      });
      alert("Rendez-vous enregistré !");
    } catch (error) {
      console.error("Erreur lors de l'enregistrement :", error);
      alert("Échec de l'enregistrement du rendez-vous.");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <select value={specialiste} onChange={(e) => setSpecialiste(e.target.value)}>
        <option value="">Choisir un spécialiste</option>
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
