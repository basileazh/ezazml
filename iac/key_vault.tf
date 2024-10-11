resource "azurerm_key_vault" "akv" {
  name                     = "${var.resource_name_prefix}-${terraform.workspace}-akv-01"
  location                 = azurerm_resource_group.rg.location
  resource_group_name      = azurerm_resource_group.rg.name
  tenant_id                = data.azurerm_client_config.current.tenant_id
  sku_name                 = "standard"
  purge_protection_enabled = false

  access_policy {
    tenant_id = var.tenant_id
    object_id = var.super_user_object_id

    secret_permissions = ["Get", "List", "Set", "Delete", "Recover", "Backup", "Restore", "Purge"]
  }

  access_policy {
    tenant_id = var.tenant_id
    object_id = azuread_service_principal.spn.object_id

    secret_permissions = ["Set", "Get", "List"]
  }
}

resource "azurerm_key_vault_secret" "client_id" {
  name         = "spn-client-id"
  value        = azuread_application_registration.app.id
  key_vault_id = azurerm_key_vault.akv.id
}

resource "azurerm_key_vault_secret" "client_secret" {
  name         = "spn-client-secret"
  value        = azuread_application_password.app_secret.value
  key_vault_id = azurerm_key_vault.akv.id
}

