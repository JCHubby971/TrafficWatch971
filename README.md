# # 🚦 TrafficWatch971 — Phase 1 (MVP)

**Plateforme d’analyse du trafic routier en Guadeloupe — Version DevOps/Cloud (Phase 1)**

TrafficWatch971 est un projet personnel visant à construire une solution de monitoring du trafic routier en Guadeloupe, avec ingestion de données, API, simulateur, visualisation et futur déploiement Cloud + Kubernetes + Terraform.

Ce dépôt correspond à la **Phase 1 : MVP local avec Docker Compose**.

---

## **Fonctionnalités (Phase 1)**

* Simulateur de trafic capable de générer :

  * vitesse moyenne
  * congestion
  * timestamp
* API FastAPI pour récupérer les mesures les plus récentes
* Base PostgreSQL accessible en local
* Architecture containerisée (Docker Compose)
* Base solide pour évolution future :

  * AWS (RDS, Lambda, Kinesis)
  * Terraform IaC
  * Kubernetes / EKS
  * Monitoring (Grafana, Prometheus)

---

## 🏗️ **Architecture Phase 1**

```
Simulator → PostgreSQL DB ← FastAPI Backend → (frontend: phase 2)
```

---

## 📂 **Arborescence**

```
TrafficWatch971/
  backend/
  simulator/
  infra/
```

---

## 🚀 **Lancer le projet**

Depuis le dossier `infra/` :

```bash
docker compose up --build
```

Quand tout est lancé :

### ▶ API :

[http://localhost:8000/traffic/latest](http://localhost:8000/traffic/latest)
[http://localhost:8000/health](http://localhost:8000/health)

### ▶ Base PostgreSQL :

localhost:5432
user: traffic
pass: traffic
db: trafficdb

### ▶ Simulateur :

Génère des données toutes les 60 secondes.

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

## 🧩 **Technologies utilisées**

* FastAPI
* PostgreSQL
* Python
* Docker & Docker Compose
* SQLAlchemy
* Pydantic

---

## 🛣️ **Roadmap**

### ✔ **Phase 1 – MVP local Docker (You are here)**

* API
* Simulation
* DB
* Docker Compose

### 🔜 **Phase 2 – Cloud & IaC**

* Terraform → AWS
* Déploiement API sur ECS ou Lambda
* RDS PostgreSQL
* CloudWatch + SNS

### 🔜 **Phase 3 – Streaming & Microservices**

* AWS Kinesis
* Services séparés (API / ingestion / analytics)
* CI/CD complet GitHub Actions

### 🔜 **Phase 4 – Kubernetes (EKS)**

* Manifests K8s
* Autoscaling
* Prometheus + Grafana

---

## 👤 **Auteur**

**Jérémy Champigny**
*(DevOps/Cloud Engineer in the making)*

---