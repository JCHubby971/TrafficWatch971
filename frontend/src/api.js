// src/api.js
const API_BASE_URL = `http://${window.location.hostname}:8000`;

export async function fetchLatestTraffic() {
  const res = await fetch(`${API_BASE_URL}/traffic/latest`);
  if (!res.ok) {
    throw new Error(`Erreur API: ${res.status}`);
  }
  return res.json();
}