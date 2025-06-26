// src/pages/ClientsList.tsx
import React, { useEffect, useState } from 'react';
import axios from '../components/axiosConfig';
import { Link } from 'react-router-dom';

interface Client {
  id: number;
  nom: string;
  prenom: string;
  telephone: string;
  courriel: string;
  nb_heures_restantes: number;
  abonnement: number;
  gestionnaire: number;
}

const ClientsList: React.FC = () => {
  const [clients, setClients] = useState<Client[]>([]);
  const token = localStorage.getItem('access');

  const fetchClients = async () => {
    try {
      const response = await axios.get('/clients/', {
        headers: { Authorization: `Bearer ${token}` },
      });
      setClients(response.data);
    } catch (error) {
      console.error('Erreur chargement des clients', error);
    }
  };

  useEffect(() => {
    fetchClients();
  }, []);

  const supprimerClient = async (id: number) => {
    if (!window.confirm("Confirmer la suppression ?")) return;
    try {
      await axios.delete(`/clients/${id}/`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      setClients(clients.filter(c => c.id !== id));
    } catch (error) {
      console.error('Erreur suppression', error);
    }
  };

  return (
    <div>
      <h2>Liste des Clients</h2>
      <ul>
        {clients.map(client => (
          <li key={client.id}>
            {client.prenom} {client.nom} – {client.courriel}
            <button onClick={() => supprimerClient(client.id)} style={{ marginLeft: 10 }}>
              Supprimer
            </button>
            <Link to={`/clients/edit/${client.id}`} style={{ marginLeft: 10 }}>
              Modifier
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ClientsList;
