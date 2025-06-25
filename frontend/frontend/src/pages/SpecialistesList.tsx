// src/pages/SpecialistesList.tsx
import React, { useEffect, useState } from 'react';
import axios from '../../components/axiosConfig';

interface Specialiste {
  id: number;
  nom: string;
  prenom: string;
  courriel: string;
  specialite: string;
}

const SpecialistesList: React.FC = () => {
  const [specialistes, setSpecialistes] = useState<Specialiste[]>([]);

  useEffect(() => {
    fetchSpecialistes();
  }, []);

  const fetchSpecialistes = async () => {
    try {
      const token = localStorage.getItem('access');
      const response = await axios.get('/specialistes/', {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setSpecialistes(response.data);
    } catch (error) {
      console.error('Erreur chargement des spécialistes', error);
    }
  };

  const deleteSpecialiste = async (id: number) => {
    if (!window.confirm("Supprimer ce spécialiste ?")) return;
    try {
      const token = localStorage.getItem('access');
      await axios.delete(`/specialistes/${id}/`, {
        headers: { Authorization: `Bearer ${token}` }
      });
      setSpecialistes(specialistes.filter(s => s.id !== id));
    } catch (error) {
      console.error("Erreur suppression", error);
    }
  };

  return (
    <div>
      <h2>Liste des spécialistes</h2>
      <ul>
        {specialistes.map(s => (
          <li key={s.id}>
            {s.prenom} {s.nom} ({s.specialite}) – {s.courriel}
            <button onClick={() => deleteSpecialiste(s.id)} style={{ marginLeft: 10 }}>🗑 Supprimer</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default SpecialistesList;
