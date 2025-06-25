// src/App.tsx
import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';

import RegisterClient from './pages/RegisterClient';
import RendezVousForm from '../components/RendezVousForm';
import NotificationsList from '../components/NotificationsList';
import NotificationBadge from '../components/NotificationBadge';
import ClientsList from './pages/ClientsList';
import Login from '../components/Login';
import GestionnairesList from './pages/GestionnairesList';
import SpecialistesList from './pages/SpecialistesList';
import EditClient from './pages/EditClient';

function App() {
  return (
    <Router>
      <div className="App">
        <header style={{ display: 'flex', justifyContent: 'space-between', padding: '10px' }}>
          <h1>Mon app GYM</h1>
          <NotificationBadge />
        </header>

        <nav style={{ margin: '10px' }}>
          <Link to="/" style={{ marginRight: 10 }}>Connexion</Link>
          <Link to="/register-client" style={{ marginRight: 10 }}>Inscription Client</Link>
          <Link to="/rendezvous" style={{ marginRight: 10 }}>Rendez-vous</Link>
          <Link to="/notifications" style={{ marginRight: 10 }}>Notifications</Link>
          <Link to="/clients" style={{ marginRight: 10 }}>Liste des clients</Link>
          <Link to="/gestionnaires" style={{ marginRight: 10 }}>Gestionnaires</Link>
          <Link to="/specialistes">Spécialistes</Link>
        </nav>

        <Routes>
          <Route path="/clients/edit/:id" element={<EditClient />} />
          <Route path="/" element={<Login />} />
          <Route path="/register-client" element={<RegisterClient />} />
          <Route path="/rendezvous" element={<RendezVousForm />} />
          <Route path="/notifications" element={<NotificationsList />} />
          <Route path="/clients" element={<ClientsList />} />
          <Route path="/gestionnaires" element={<GestionnairesList />} />
          <Route path="/specialistes" element={<SpecialistesList />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
