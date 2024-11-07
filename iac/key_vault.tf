# Key Vault Resource

resource "azurerm_key_vault" "akv" {
  name                     = "${var.resource_name_prefix}-${terraform.workspace}-akv-01"
  location                 = azurerm_resource_group.rg.location
  resource_group_name      = azurerm_resource_group.rg.name
  tenant_id                = data.azurerm_client_config.current.tenant_id
  sku_name                 = "standard"
  purge_protection_enabled = false
}

# Give the DevOPS SPN access to the Key Vault as a Key Vault Contributor + access policy

resource "azurerm_role_assignment" "akv_kv_contributor_devops_spn" {
  principal_id         = var.devops_spn_object_id
  role_definition_name = "Key Vault Contributor"
  scope                = azurerm_key_vault.akv.id
}

resource "azurerm_key_vault_access_policy" "akv_access_policy_devops_spn" {
  key_vault_id = azurerm_key_vault.akv.id
  tenant_id    = data.azurerm_client_config.current.tenant_id
  object_id    = var.devops_spn_object_id

  secret_permissions = [
    "Get",
    "List",
    "Set",
    "Delete",
    "Recover",
    "Backup",
    "Restore",
    "Purge",
  ]
}

# Give the Project SPN access to the Key Vault as access policy
resource "azurerm_key_vault_access_policy" "akv_access_policy_project_spn" {
  key_vault_id = azurerm_key_vault.akv.id
  tenant_id    = data.azurerm_client_config.current.tenant_id
  object_id    = azuread_application_registration.app.object_id

  secret_permissions = [
    "Get",
    "List",
    "Set",
    "Delete",
  ]
}

# Create 2 secrets in the Key Vault
# TODO: include these secrets from the Key Vault
# resource "azurerm_key_vault_secret" "client_id" {
#   name         = "spn-client-id"
#   value        = azuread_application_registration.app.id
#   key_vault_id = azurerm_key_vault.akv.id
# }

# resource "azurerm_key_vault_secret" "client_secret" {
#   name         = "spn-client-secret"
#   value        = azuread_application_password.app_secret.value
#   key_vault_id = azurerm_key_vault.akv.id
# }