# Auth variables

variable "enterprise_application_name" {
  type        = string
  description = "Enterprise Application Name"
  default     = "ezazml-app-dev-01"
}

variable "user_principal_name_prefix" {
  type        = string
  description = "User Principal Name before @"

}

variable "user_display_name" {
  type        = string
  description = "User Display Name"
}

variable "user_password" {
  type        = string
  description = "User Password"
}

variable "tenant_id" {
  type        = string
  description = "Azure Tenant ID"
}

# Resource variables

variable "environment" {
  type        = string
  description = "Name of the environment"
  default     = "dev"
}

variable "location" {
  type        = string
  description = "Location of the resources"
  default     = "eastus"
}

variable "prefix" {
  type        = string
  description = "Prefix of the resource name"
  default     = "ml"
}