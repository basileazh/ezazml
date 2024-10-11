.PHONY: tf-init tf-plan tf-apply login-spn tf-import-rg

tf-init:
	terraform init
	terraform workspace new $(TF_WORKSPACE) ||
	terraform workspace select $(TF_WORKSPACE)

tf-select-ws:
	terraform workspace select $(TF_WORKSPACE)

tf-upgrade:
	terraform init -upgrade

tf-import-rg:
	terraform import -var-file="${TF_VAR_FILE_PATH}" azurerm_resource_group.default /subscriptions/$(AZURE_SUBSCRIPTION_ID)/resourceGroups/$(AML_RESOURCE_GROUP)

tf-import-aml:
	terraform import -var-file="${TF_VAR_FILE_PATH}" azurerm_machine_learning_workspace.default /subscriptions/$(AZURE_SUBSCRIPTION_ID)/resourceGroups/$(AML_RESOURCE_GROUP)/providers/Microsoft.MachineLearningServices/workspaces/$(AML_WORKSPACE_NAME)

tf-plan:
	terraform plan -out "../env/$(TF_WORKSPACE)/$(TF_OUTPUT_NAME)"

tf-apply:
	terraform apply "../env/$(TF_WORKSPACE)/$(TF_OUTPUT_NAME)"

tf-apply-aa:
	terraform apply -auto-approve

tf-destroy:
	terraform destroy

tf-destroy-aa:
	terraform destroy -auto-approve