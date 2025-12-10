terraform {
  required_version = ">= 1.6.0"

  required_providers {
    ovh = {
      source  = "ovh/ovh"
      version = "~> 1.0"
    }
  }
}

provider "ovh" {
  endpoint           = "ovh-eu"

  # ⚠️ Ces variables NE DOIVENT PAS être hardcodées.
  # On les passera via variables Terraform ou via variables d'environnement.
  application_key    = var.ovh_application_key
  application_secret = var.ovh_application_secret
  consumer_key       = var.ovh_consumer_key
}