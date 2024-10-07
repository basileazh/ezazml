# Dependent resources for Azure Machine Learning
resource "azurerm_application_insights" "default" {
  name                = "${var.prefix}-${var.environment}-appi-01"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  application_type    = "web"
}

resource "azurerm_key_vault" "default" {
  name                     = "${var.prefix}-${var.environment}-akv-01"
  location                 = azurerm_resource_group.rg.location
  resource_group_name      = azurerm_resource_group.rg.name
  tenant_id                = data.azurerm_client_config.current.tenant_id
  sku_name                 = "standard"
  purge_protection_enabled = false
}

resource "azurerm_storage_account" "default" {
  name                            = "${var.prefix}${var.environment}asa01"
  location                        = azurerm_resource_group.rg.location
  resource_group_name             = azurerm_resource_group.rg.name
  account_tier                    = "Standard"
  account_replication_type        = "GRS"
  allow_nested_items_to_be_public = false
}

resource "azurerm_container_registry" "default" {
  name                = "${var.prefix}${var.environment}acr01"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  sku                 = "Premium"
  admin_enabled       = true
}

# Machine Learning workspace
resource "azurerm_machine_learning_workspace" "default" {
  name                          = "${var.prefix}-${var.environment}-aml-w01"
  location                      = azurerm_resource_group.rg.location
  resource_group_name           = azurerm_resource_group.rg.name
  application_insights_id       = azurerm_application_insights.default.id
  key_vault_id                  = azurerm_key_vault.default.id
  storage_account_id            = azurerm_storage_account.default.id
  container_registry_id         = azurerm_container_registry.default.id
  public_network_access_enabled = true

  identity {
    type = "SystemAssigned"
  }
}


