# ✅ **2. README du dossier Terraform**


# 🌩️ TrafficWatch971 — Terraform (Phase 3)

Ce dossier contient l'infrastructure AWS préparée pour la migration future du projet.

## Objectifs Phase 3 (AWS Cloud + IaC)
- Déployer la base PostgreSQL sur AWS RDS
- Déployer l'API FastAPI (ECS Fargate ou EC2)
- Créer les réseaux (VPC, subnets, routage, gateways)
- Exposer l’API via un load balancer (ALB)
- Préparer le streaming pour Phase 4 (Kinesis)

## Contenu actuel
- VPC `10.10.0.0/16`
- 2 subnets publics (AZ A & B)
- Internet Gateway
- Route table publique
- Variables `project_name` & `aws_region`

> ⚠️ **Aucune ressource n’est déployée tant que le compte AWS n’est pas activé.**