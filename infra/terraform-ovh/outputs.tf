output "project_name" {
  value       = local.project_name
  description = "Nom logique du projet"
}

output "vps_ipv4" {
  value       = var.vps_ipv4
  description = "Adresse IPv4 publique du VPS utilisée par TrafficWatch971"
}

output "dns_record" {
  value       = var.domain_name != "" ? "${var.subdomain}.${var.domain_name}" : "DNS non configuré (domain_name vide)"
  description = "Nom de domaine (si configuré) pointant vers le VPS"
}