variable "aws_region" {
  description = "AWS region where to deploy TrafficWatch971"
  type        = string
  default     = "eu-west-3" # Paris (on pourra changer)
}

variable "project_name" {
  description = "Base name for AWS resources"
  type        = string
  default     = "trafficwatch971"
}