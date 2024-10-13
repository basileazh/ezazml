output "application_client_id" {
  value = azuread_application_registration.app.client_id
}

output "key_vault_name" {
  value = azurerm_key_vault.akv.name
}

output "machine_learning_workspace_id" {
  value = azurerm_machine_learning_workspace.default.id
}

output "machine_learning_workspace_name" {
  value = azurerm_machine_learning_workspace.default.name
}

output "storage_container_name" {
  value = azurerm_storage_container.example.name
}

output "container_registry_name" {
  value = azurerm_container_registry.default.name
}

output "application_insights_name" {
  value = azurerm_application_insights.default.name
}
