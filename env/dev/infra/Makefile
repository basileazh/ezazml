.PHONY: tf-init tf-plan tf-apply login-spn tf-import-rg

tf-init:
	terraform init

tf-upgrade:
	terraform init -upgrade

tf-import-rg:
	terraform import -var-file="${TF_VAR_FILE_PATH}" azurerm_resource_group.default /subscriptions/$(AZURE_SUBSCRIPTION_ID)/resourceGroups/$(RG_NAME)

tf-import-aml:
	terraform import -var-file="${TF_VAR_FILE_PATH}" azurerm_machine_learning_workspace.default /subscriptions/$(AZURE_SUBSCRIPTION_ID)/resourceGroups/$(RG_NAME)/providers/Microsoft.MachineLearningServices/workspaces/$(AML_WORKSPACE_NAME)

tf-plan:
	terraform plan -var-file "${TF_VAR_FILE_PATH}" -out "${TF_OUTPUT_PATH}"

tf-apply:
	terraform apply $(TF_OUTPUT_PATH)

tf-apply-aa:
	terraform apply -auto-approve