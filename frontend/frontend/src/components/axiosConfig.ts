import axios from 'axios';

const instance = axios.create({
  baseURL: 'https://gestion-gym-backend.onrender.com',
  withCredentials: true,
});

instance.interceptors.request.use((config) => {
  const token = localStorage.getItem('access');
  if (token && config.headers) {
    config.headers['Authorization'] = `Bearer ${token}`;
  }
  return config;
});

export default instance;
