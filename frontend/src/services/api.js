import axios from "axios";
import { getUser, logout } from "./auth";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL
});

api.interceptors.request.use(config => {
  const u = getUser();
  if (u?.access_token) {
    config.headers.Authorization = `Bearer ${u.access_token}`;
  }
  return config;
});

api.interceptors.response.use(
  r => r,
  e => {
    if (e.response?.status === 401) logout();
    return Promise.reject(e);
  }
);

export default api;
