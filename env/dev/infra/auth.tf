data "azuread_client_config" "current" {}

# Retrieve domain information
data "azuread_domains" "domains" {
  only_initial = true
}

resource "azuread_application" "app" {
  display_name = "ezazml-app"
  owners       = [data.azuread_client_config.current.object_id]
}

resource "azuread_service_principal" "spn" {
  client_id                    = azuread_application.app.client_id
  app_role_assignment_required = false
  owners                       = [data.azuread_client_config.current.object_id]
}

# Create a user
resource "azuread_user" "user1" {
  user_principal_name = format("%s%s", var.user_principal_name_prefix, "@${data.azuread_domains.domains.domains.0.domain_name}")
  display_name        = var.user_display_name
  password            = var.user_password
}