# Compute instance
resource "azurerm_machine_learning_compute_instance" "main" {
  count = terraform.workspace == "dev" ? var.compute_instance_count_dev : var.compute_instance_count_prd

  name                          = "${var.resource_name_prefix}-${terraform.workspace}-instance-w01"
  machine_learning_workspace_id = azurerm_machine_learning_workspace.default.id
  virtual_machine_size          = var.compute_instance_size_dev
}

# Compute Cluster

resource "azurerm_machine_learning_compute_cluster" "compute" {
  count = terraform.workspace == "dev" ? var.compute_cluster_count_dev : var.compute_cluster_count_prd

  name                          = "${var.resource_name_prefix}-${terraform.workspace}-cpu-cluster-w01"
  location                      = azurerm_resource_group.rg.location
  machine_learning_workspace_id = azurerm_machine_learning_workspace.default.id
  vm_priority                   = terraform.workspace == "dev" ? var.compute_cluster_priority_dev : var.compute_cluster_priority_prd
  vm_size                       = terraform.workspace == "dev" ? var.compute_cluster_size_dev : var.compute_cluster_size_prd

  identity {
    type = "SystemAssigned"
  }

  scale_settings {
    min_node_count                       = terraform.workspace == "dev" ? var.compute_cluster_scale_min_node_dev : var.compute_cluster_scale_min_node_prd
    max_node_count                       = terraform.workspace == "dev" ? var.compute_cluster_scale_max_node_dev : var.compute_cluster_scale_max_node_prd
    scale_down_nodes_after_idle_duration = "PT10M" # 10 minutes
  }

}
