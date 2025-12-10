locals {
  project_name = var.project_name
}

# Ici, on prépare l'infra autour de mon VPS OVH.
# Exemple : gestion DNS pour pointer un sous-domaine vers l'IP du VPS.

# Cette ressource est un EXEMPLE pour plus tard.
# Elle suppose que j'ai un domaine géré chez OVH (ex: mon-domaine.ovh).
# Je pourrais la commenter/décommenter quand j'aurai un domaine.

resource "ovh_domain_zone_record" "trafficwatch_a_record" {
  count = var.domain_name != "" ? 1 : 0

  zone      = var.domain_name
  subdomain = var.subdomain
  fieldtype = "A"
  target    = var.vps_ipv4
  ttl       = 3600
}

# On pourrait ajouter plus tard :
# - des enregistrements AAAA (IPv6)
# - des enregistrements CNAME
# - d'autres services OVHcloud (Public Cloud, storage, etc.)