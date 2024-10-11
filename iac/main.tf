data "azurerm_client_config" "current" {}

resource "azurerm_resource_group" "rg" {
  name     = "${var.resource_name_prefix}-${terraform.workspace}-rg"
  location = var.location
}
