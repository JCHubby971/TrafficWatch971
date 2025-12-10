# 🌩️ TrafficWatch971 — Terraform OVH (VPS / DNS / Cloud)

Ce dossier contient une configuration Terraform basée sur le provider **OVHcloud**, pour gérer l'infrastructure liée au projet TrafficWatch971 côté OVH.

## Objectifs

- Documenter et automatiser l'infrastructure autour du VPS OVH
- Préparer la gestion :
  - du DNS (nom de domaine pointant vers le VPS)
  - de futures ressources OVHcloud (Public Cloud, load balancer, stockage...)

## Provider

Le provider utilisé est :

- `ovh/ovh` (Terraform Registry)

Les identifiants OVH ne sont **jamais** commités dans le dépôt.  
Ils doivent être fournis via :
- des variables d'environnement, ou
- un fichier `.tfvars` ignoré par git.

## Futur

- Ajouter une ressource DNS pour exposer le dashboard via un nom de domaine
- Ajouter du firewall, des règles de sécurité, etc.
- (Optionnel) Gérer des instances Public Cloud / services managés OVH