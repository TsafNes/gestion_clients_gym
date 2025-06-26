import React, { useState, useEffect } from 'react';
import axios from '../components/axiosConfig';


const RegisterClient: React.FC = () => {
  const [formData, setFormData] = useState({
    nom: '',
    prenom: '',
    telephone: '',
    courriel: '',
    nb_heures_restantes: 10,
    abonnement: '',
    gestionnaire: ''
  });

  const [abonnements, setAbonnements] = useState([]);
  const [gestionnaires, setGestionnaires] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/abonnements/')
      .then(res => setAbonnements(res.data))
      .catch(err => console.error('Erreur chargement abonnements', err));

    axios.get('http://127.0.0.1:8000/api/gestionnaires/')
      .then(res => setGestionnaires(res.data))
      .catch(err => console.error('Erreur chargement gestionnaires', err));
  }, []);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await axios.post('http://127.0.0.1:8000/api/clients/', formData);
      alert('Client inscrit avec succès');
    } catch (error) {
      alert("Erreur lors de l'inscription");
      console.error(error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="nom" placeholder="Nom" onChange={handleChange} /><br />
      <input name="prenom" placeholder="Prénom" onChange={handleChange} /><br />
      <input name="telephone" placeholder="Téléphone" onChange={handleChange} /><br />
      <input name="courriel" placeholder="Courriel" onChange={handleChange} /><br />

      <select name="abonnement" onChange={handleChange} required>
        <option value="">-- Sélectionner un abonnement --</option>
        {abonnements.map((ab: any) => (
          <option key={ab.id} value={ab.id}>
            {ab.type} ({ab.date_debut} → {ab.date_fin})
          </option>
        ))}
      </select><br />

      <select name="gestionnaire" onChange={handleChange} required>
        <option value="">-- Sélectionner un gestionnaire --</option>
        {gestionnaires.map((gest: any) => (
          <option key={gest.id} value={gest.id}>
            {gest.prenom} {gest.nom}
          </option>
        ))}
      </select><br />

      <button type="submit">S’inscrire</button>
    </form>
  );
};

export default RegisterClient;
