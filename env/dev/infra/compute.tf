# Compute instance
resource "azurerm_machine_learning_compute_instance" "main" {
  name                          = "${var.prefix}-${var.environment}-instance-w01"
  machine_learning_workspace_id = azurerm_machine_learning_workspace.default.id
  virtual_machine_size          = "STANDARD_DS2_V2"
}

# Compute Cluster
resource "azurerm_machine_learning_compute_cluster" "compute" {
  name                          = "${var.prefix}-${var.environment}-cpu-cluster-w01"
  location                      = azurerm_resource_group.rg.location
  machine_learning_workspace_id = azurerm_machine_learning_workspace.default.id
  vm_priority                   = "Dedicated"
  vm_size                       = "STANDARD_DS2_V2"

  identity {
    type = "SystemAssigned"
  }

  scale_settings {
    min_node_count                       = 0
    max_node_count                       = 3
    scale_down_nodes_after_idle_duration = "PT15M" # 15 minutes
  }

}
