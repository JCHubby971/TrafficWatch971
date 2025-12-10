variable "project_name" {
  description = "Nom logique du projet (pour tagging / organisation)"
  type        = string
  default     = "trafficwatch971"
}

variable "ovh_application_key" {
  description = "OVH API application key"
  type        = string
  sensitive   = true
}

variable "ovh_application_secret" {
  description = "OVH API application secret"
  type        = string
  sensitive   = true
}

variable "ovh_consumer_key" {
  description = "OVH API consumer key"
  type        = string
  sensitive   = true
}

variable "vps_ipv4" {
  description = "Adresse IPv4 publique du VPS OVH (ex: 54.xx.xxx.xx)"
  type        = string
}

variable "domain_name" {
  description = "Nom de domaine géré chez OVH (ex: mon-domaine.ovh)"
  type        = string
  default     = ""
}

variable "subdomain" {
  description = "Sous-domaine à utiliser pour TrafficWatch971 (ex: traffic)"
  type        = string
  default     = "traffic"
}