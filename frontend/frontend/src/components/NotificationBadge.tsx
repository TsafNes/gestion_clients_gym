import React, { useEffect, useState } from 'react';
import axios from './axiosConfig';

export default function NotificationBadge() {
  const [nonLues, setNonLues] = useState<number>(0);

  const fetchNonLues = async () => {
    try {
      const res = await axios.get('/api/notifications/');
      const count = res.data.filter((n: any) => !n.lu).length;
      setNonLues(count);
    } catch (error) {
      console.error("Erreur chargement notifications :", error);
    }
  };

  useEffect(() => {
    fetchNonLues();

    // Optionnel : actualiser toutes les 30s
    const interval = setInterval(fetchNonLues, 30000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div style={{ position: 'relative', display: 'inline-block' }}>
      <span role="img" aria-label="cloche">🔔</span>
      {nonLues > 0 && (
        <span style={{
          position: 'absolute',
          top: -5,
          right: -5,
          backgroundColor: 'red',
          color: 'white',
          borderRadius: '50%',
          padding: '2px 6px',
          fontSize: '12px'
        }}>
          {nonLues}
        </span>
      )}
    </div>
  );
}
