# Entra ID Authentication Application

data "azuread_application_published_app_ids" "well_known" {}

data "azuread_service_principal" "msgraph" {
  client_id = data.azuread_application_published_app_ids.well_known.result["MicrosoftGraph"]
}

data "azuread_client_config" "current" {}

# Retrieve domain information
data "azuread_domains" "domains" {
  only_initial = true
}

resource "azuread_application_registration" "app" {
  display_name = "${var.auth_application_name_prefix}-${terraform.workspace}-01"
}

resource "azuread_application_password" "app_secret" {
  application_id = azuread_application_registration.app.id
}

resource "azuread_service_principal" "spn" {
  client_id                    = azuread_application_registration.app.client_id
  app_role_assignment_required = false
  owners                       = [data.azuread_client_config.current.object_id]
}

# Grant the Service Principal Contributor access to the Resource Group and to the Storage Account where the Terraform backend is stored

resource "azurerm_role_assignment" "rg_contributor_spn" {
  principal_id         = azuread_service_principal.spn.object_id
  role_definition_name = "Contributor"
  scope                = azurerm_resource_group.rg.id
}

resource "azurerm_role_assignment" "spn_storage_contributor" {
  principal_id         = azuread_service_principal.spn.object_id
  role_definition_name = "Storage Account Contributor"
  scope                = var.tf_backend_storage_account_id
}

# Create a user
resource "azuread_user" "user1" {
  user_principal_name = "${var.user_principal_name_prefix}@${data.azuread_domains.domains.domains.0.domain_name}"
  display_name        = var.user_display_name
  password            = var.user_password
}