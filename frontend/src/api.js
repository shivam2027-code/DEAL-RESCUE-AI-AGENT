import axios from "axios";

// In production (served by FastAPI), baseURL is "" (same origin).
// In local dev, Vite proxy forwards /api → localhost:8000.
const API = axios.create({
  baseURL: import.meta.env.VITE_API_URL || "",
});

export default API;
