// src/App.jsx
import React, { useEffect, useState } from "react";
import { fetchLatestTraffic } from "./api";
import { TrafficTable } from "./components/TrafficTable";
import "./App.css";

function App() {
  const [traffic, setTraffic] = useState([]);
  const [lastUpdate, setLastUpdate] = useState(null);
  const [error, setError] = useState("");

  async function loadTraffic() {
    try {
      setError("");
      const data = await fetchLatestTraffic();
      setTraffic(data);
      setLastUpdate(new Date());
    } catch (err) {
      console.error(err);
      setError("Erreur lors du chargement des données.");
    }
  }

  useEffect(() => {
    loadTraffic();
    const interval = setInterval(loadTraffic, 15000); // refresh toutes les 15s
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="app">
      <header>
        <h1>TrafficWatch971 - Dashboard temps réel</h1>
        {lastUpdate && (
          <p className="status">
            Dernière mise à jour : {lastUpdate.toLocaleTimeString()}
          </p>
        )}
        {error && <p className="error">{error}</p>}
      </header>

      <main>
        {traffic.length === 0 && !error ? (
          <p>Aucune donnée pour le moment...</p>
        ) : (
          <TrafficTable data={traffic} />
        )}
      </main>
    </div>
  );
}

export default App;