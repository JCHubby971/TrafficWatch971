// src/components/TrafficTable.jsx
import React from "react";

function congestionLabel(level) {
    if (level < 30) return { text: `${level}% (fluide)`, className: "badge badge-good" };
    if (level < 70) return { text: `${level}% (chargé)`, className: "badge badge-warn" };
    return { text: `${level}% (bouchon)`, className: "badge badge-bad" };
}

export function TrafficTable({ data }) {
    return (
        <table className="traffic-table">
            <thead>
                <tr>
                    <th>Segment</th>
                    <th>Vitesse (km/h)</th>
                    <th>Congestion</th>
                    <th>Horodatage</th>
                </tr>
            </thead>
            <tbody>
                {data.map((item, idx) => {
                    const badge = congestionLabel(item.congestion_level);
                    return (
                        <tr key={`${item.segment_name}-${item.timestamp}-${idx}`}>
                            <td>{item.segment_name}</td>
                            <td>{item.avg_speed_kmh.toFixed(1)}</td>
                            <td>
                                <span className={badge.className}>{badge.text}</span>
                            </td>
                            <td>{new Date(item.timestamp).toLocaleString()}</td>
                        </tr>
                    );
                })}
            </tbody>
        </table>
    );
}