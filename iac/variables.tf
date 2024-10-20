# Auth variables
variable "directory_object_id" {
  type        = string
  description = "Azure Directory Object ID"
}

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

# Storage Account variables

variable "adls_container_name" {
  type        = string
  description = "Name of the ADLS container"
  default     = "main"
}

# Compute variables

variable "compute_instance_size_dev" {
  type        = string
  description = "Size of the compute instance"
  default     = "Standard_A1_v2"
}

variable "compute_cluster_size_dev" {
  type        = string
  description = "Size of the compute cluster"
  default     = "Standard_A1_v2"
}

variable "compute_cluster_size_prd" {
  type        = string
  description = "Size of the compute cluster"
  default     = "Standard_A1_v2"
}

variable "compute_instance_count_dev" {
  type        = number
  description = "Size of the compute instance"
  default     = 0
}

variable "compute_instance_count_prd" {
  type        = number
  description = "Size of the compute instance"
  default     = 0
}

variable "compute_cluster_count_dev" {
  type        = number
  description = "Size of the compute cluster"
  default     = 1
}

variable "compute_cluster_count_prd" {
  type        = number
  description = "Size of the compute cluster"
  default     = 1
}

variable "compute_cluster_priority_dev" {
  type        = string
  description = "Priority of the compute cluster"
  default     = "LowPriority"
}

variable "compute_cluster_priority_prd" {
  type        = string
  description = "Priority of the compute cluster"
  default     = "LowPriority"
}

variable "compute_cluster_scale_min_node_dev" {
  type        = number
  description = "Minimum number of nodes in the cluster"
  default     = 0
}

variable "compute_cluster_scale_min_node_prd" {
  type        = number
  description = "Minimum number of nodes in the cluster"
  default     = 0
}

variable "compute_cluster_scale_max_node_dev" {
  type        = number
  description = "Maximum number of nodes in the cluster"
  default     = 3
}

variable "compute_cluster_scale_max_node_prd" {
  type        = number
  description = "Maximum number of nodes in the cluster"
  default     = 3
}
