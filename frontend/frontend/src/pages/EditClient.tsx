import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import axios from '../../components/axiosConfig';

interface Client {
  nom: string;
  prenom: string;
  telephone: string;
  courriel: string;
  nb_heures_restantes: number;
  abonnement: number;
  gestionnaire: number;
}

const EditClient: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();

  const [clientData, setClientData] = useState<Client>({
    nom: '',
    prenom: '',
    telephone: '',
    courriel: '',
    nb_heures_restantes: 0,
    abonnement: 0,
    gestionnaire: 0
  });

  const [abonnements, setAbonnements] = useState([]);
  const [gestionnaires, setGestionnaires] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const clientRes = await axios.get(`/clients/${id}/`);
        setClientData(clientRes.data);

        const abRes = await axios.get('/abonnements/');
        setAbonnements(abRes.data);

        const gestRes = await axios.get('/gestionnaires/');
        setGestionnaires(gestRes.data);
      } catch (error) {
        console.error("Erreur chargement des données", error);
      }
    };

    fetchData();
  }, [id]);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    setClientData({ ...clientData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await axios.put(`/clients/${id}/`, clientData);
      alert("Client mis à jour avec succès !");
      navigate('/clients');
    } catch (error) {
      console.error("Erreur lors de la mise à jour", error);
      alert("Erreur lors de la mise à jour du client");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Modifier un client</h2>
      <input name="nom" value={clientData.nom} onChange={handleChange} placeholder="Nom" /><br />
      <input name="prenom" value={clientData.prenom} onChange={handleChange} placeholder="Prénom" /><br />
      <input name="telephone" value={clientData.telephone} onChange={handleChange} placeholder="Téléphone" /><br />
      <input name="courriel" value={clientData.courriel} onChange={handleChange} placeholder="Courriel" /><br />
      <input
        name="nb_heures_restantes"
        type="number"
        value={clientData.nb_heures_restantes}
        onChange={handleChange}
        placeholder="Heures restantes"
      /><br />

      <select name="abonnement" value={clientData.abonnement} onChange={handleChange}>
        <option value="">-- Abonnement --</option>
        {abonnements.map((ab: any) => (
          <option key={ab.id} value={ab.id}>
            {ab.type} ({ab.date_debut} → {ab.date_fin})
          </option>
        ))}
      </select><br />

      <select name="gestionnaire" value={clientData.gestionnaire} onChange={handleChange}>
        <option value="">-- Gestionnaire --</option>
        {gestionnaires.map((gest: any) => (
          <option key={gest.id} value={gest.id}>
            {gest.prenom} {gest.nom}
          </option>
        ))}
      </select><br />

      <button type="submit">Enregistrer</button>
    </form>
  );
};

export default EditClient;
