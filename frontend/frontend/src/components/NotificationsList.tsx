import React, { useEffect, useState } from 'react';
import axios from './axiosConfig';

interface Notification {
  id: number;
  message: string;
  date: string;
  lu: boolean;
}

export default function NotificationsList() {
  const [notifications, setNotifications] = useState<Notification[]>([]);

  const fetchNotifications = async () => {
    try {
      const response = await axios.get('/api/notifications/');
      setNotifications(response.data);
    } catch (error) {
      console.error('Erreur lors du chargement des notifications :', error);
    }
  };

  const marquerCommeLu = async (id: number) => {
    try {
      await axios.patch(`/api/notifications/${id}/`, { lu: true });
      fetchNotifications(); // recharge la liste après mise à jour
    } catch (error) {
      console.error('Erreur lors du marquage :', error);
    }
  };

  useEffect(() => {
    fetchNotifications();
  }, []);

  return (
    <div>
      <h3>🔔 Notifications</h3>
      <ul>
        {notifications.map((notif) => (
          <li key={notif.id} style={{ opacity: notif.lu ? 0.5 : 1 }}>
            <p>{notif.message} – <em>{new Date(notif.date).toLocaleString()}</em></p>
            {!notif.lu && (
              <button onClick={() => marquerCommeLu(notif.id)}>
                Marquer comme lu
              </button>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}
