// src/components/Notifications.tsx

import React, { useEffect, useState } from 'react';
import axios from './axiosConfig';

interface Notification {
  id: number;
  message: string;
  date: string;
}

const Notifications: React.FC = () => {
  const [notifications, setNotifications] = useState<Notification[]>([]);
  const [error, setError] = useState('');

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/notifications/', {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}` // token JWT stocké après login
      }
    })
    .then(response => {
      setNotifications(response.data);
    })
    .catch(error => {
      setError("Erreur lors du chargement des notifications");
      console.error(error);
    });
  }, []);

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">Notifications</h2>
      {error && <p className="text-red-500">{error}</p>}
      <ul>
        {notifications.map((n) => (
          <li key={n.id} className="border-b py-2">
            {n.message} – <span className="text-sm text-gray-500">{new Date(n.date).toLocaleString()}</span>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Notifications;
