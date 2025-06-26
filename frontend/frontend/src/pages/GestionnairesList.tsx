// src/pages/GestionnairesList.tsx
import React, { useEffect, useState } from 'react';
import axios from '../components/axiosConfig';

interface Gestionnaire {
  id: number;
  nom: string;
  prenom: string;
  courriel: string;
}

const GestionnairesList: React.FC = () => {
  const [gestionnaires, setGestionnaires] = useState<Gestionnaire[]>([]);

  useEffect(() => {
    fetchGestionnaires();
  }, []);

  const fetchGestionnaires = async () => {
    try {
      const token = localStorage.getItem('access');
      const response = await axios.get('/gestionnaires/', {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setGestionnaires(response.data);
    } catch (error) {
      console.error('Erreur chargement des gestionnaires', error);
    }
  };

  const deleteGestionnaire = async (id: number) => {
    if (!window.confirm("Supprimer ce gestionnaire ?")) return;
    try {
      const token = localStorage.getItem('access');
      await axios.delete(`/gestionnaires/${id}/`, {
        headers: { Authorization: `Bearer ${token}` }
      });
      setGestionnaires(gestionnaires.filter(g => g.id !== id));
    } catch (error) {
      console.error("Erreur suppression", error);
    }
  };

  return (
    <div>
      <h2>Liste des gestionnaires</h2>
      <ul>
        {gestionnaires.map(g => (
          <li key={g.id}>
            {g.prenom} {g.nom} – {g.courriel}
            <button onClick={() => deleteGestionnaire(g.id)} style={{ marginLeft: 10 }}>🗑 Supprimer</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default GestionnairesList;
