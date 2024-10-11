# Backend variables
variable "backend_resource_name" {
  type        = string
  description = "Resource Name"
  default     = "terraform-state-rg"
}

variable "backend_storage_account_name" {
  type        = string
  description = "Storage Account Name"
  default     = "terraformbackendasa"
}

variable "backend_container_name" {
  type        = string
  description = "Container Name"
  default     = "tfstate"
}

variable "backend_terraform_state_key" {
  type        = string
  description = "Terraform State Key"
  default     = "terraform.tfstate"
}


# Auth variables

variable "super_user_object_id" {
  type        = string
  description = "Super User Object ID"
}

variable "auth_application_name_prefix" {
  type        = string
  description = "Application Name"
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

variable "location" {
  type        = string
  description = "Location of the resources"
  default     = "eastus"
}

variable "resource_name_prefix" {
  type        = string
  description = "Prefix of the resource name"
  default     = "ml"
}