# 🚦 TrafficWatch971 — Plateforme d’analyse du trafic routier en Guadeloupe

**Projet DevOps/Cloud — MVP + Déploiement VPS + Préparation AWS Terraform**

TrafficWatch971 est une plateforme qui collecte, simule et expose des données de trafic routier en Guadeloupe.  
Le projet suit une montée en puissance progressive : MVP en local, déploiement sur VPS OVH, puis migration AWS avec Terraform, streaming, et Kubernetes.

Ce dépôt correspond à la **Phase 1 & Phase 2** :
- Phase 1 : MVP local avec Docker Compose  
- Phase 2 : Déploiement sur VPS OVH (prod actuelle)

---

## ✅ Fonctionnalités actuelles

### Phase 1 – MVP (local)
- Simulateur Python générant :
  - vitesse moyenne (km/h)
  - niveau de congestion (%)
  - timestamp
- API FastAPI exposant `/traffic/latest` + `/health`
- Base de données PostgreSQL
- Architecture containerisée (Docker Compose)

### Phase 2 – Déploiement VPS OVH (prod)
- VPS Ubuntu 22.04
- Docker + Docker Compose installés
- Stack déployée automatiquement via `docker compose up -d`
- Dashboard frontend **accessible publiquement**
- Simulation + backend + DB en production

---

## 🏗️ Architecture Phase 1

```

Simulator → PostgreSQL DB ← FastAPI Backend ← Frontend (React)

```

---

## 📂 Arborescence du projet

```

TrafficWatch971/
backend/         → API FastAPI
simulator/       → Générateur de données
frontend/        → Dashboard React
infra/
├─ docker-compose.yml
└─ terraform/ → Phase 3 : infra AWS (VPC déjà décrite)

````

---

## 🚀 Lancer le projet localement

Depuis le dossier `infra/` :

```bash
docker compose up --build
````

### Endpoints API

* [http://localhost:8000/traffic/latest](http://localhost:8000/traffic/latest)
* [http://localhost:8000/health](http://localhost:8000/health)

### Base PostgreSQL (local)

* host: localhost
* port: 5432
* user: traffic
* password: traffic
* database: trafficdb

---

## 📊 Exemple de sortie API

```json
[
  {
    "segment_name": "Jarry → Pointe-à-Pitre",
    "avg_speed_kmh": 34,
    "congestion_level": 66,
    "timestamp": "2025-01-01T12:00:00Z"
  }
]
```

---

## 🛠️ Technologies utilisées

* FastAPI
* PostgreSQL
* Docker & Docker Compose
* SQLAlchemy
* Python
* React (frontend)
* Terraform (Phase 3+)
* AWS (à venir)

---

## 🛣️ Roadmap du projet

### ✔ **Phase 1 — MVP local Docker (terminée)**

* API
* Simulation
* DB
* Docker Compose

### ✔ **Phase 2 — Déploiement VPS OVH (terminée)**

* Installation Docker sur VPS
* Déploiement complet
* Dashboard public en temps réel

### 🔜 **Phase 3 — Cloud & IaC (AWS dès activation de mon compte)**

* Terraform : VPC, subnets, routage (déjà écrit dans `infra/terraform`)
* Déploiement API (ECS Fargate)
* Base PostgreSQL → RDS
* Logs + Monitoring → CloudWatch

### 🔜 Phase 4 — Streaming & Microservices

* AWS Kinesis (ingestion)
* Microservices ingestion / analytics
* CI/CD GitHub Actions

### 🔜 Phase 5 — Kubernetes (EKS)

* Manifests K8s
* Autoscaling
* Monitoring Prometheus + Grafana

---

## 👤 Auteur

**Jérémy Champigny**
*(DevOps/Cloud Engineer in the making)*