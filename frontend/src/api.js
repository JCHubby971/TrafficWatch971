// src/api.js
const API_URL = "http://localhost:8000";

export async function fetchLatestTraffic() {
  const res = await fetch(`${API_URL}/traffic/latest`);
  if (!res.ok) {
    throw new Error(`Erreur API: ${res.status}`);
  }
  return res.json();
}