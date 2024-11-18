.PHONY: tf-init tf-select-ws tf-upgrade tf-import-rg tf-import-aml tf-plan-no-input tf-plan-output tf-apply tf-apply-aa tf-destroy tf-destroy-aa

TF_WORKSPACE ?= dev
TF_OUTPUT_NAME ?= tfplan

tf-init:
	terraform init

tf-upgrade:
	terraform init -upgrade

tf-import-rg:
	terraform import -var-file="${TF_VAR_FILE_PATH}" azurerm_resource_group.default /subscriptions/$(ARM_SUBSCRIPTION_ID)/resourceGroups/$(AML_RESOURCE_GROUP)

tf-import-aml:
	terraform import -var-file="${TF_VAR_FILE_PATH}" azurerm_machine_learning_workspace.default /subscriptions/$(ARM_SUBSCRIPTION_ID)/resourceGroups/$(AML_RESOURCE_GROUP)/providers/Microsoft.MachineLearningServices/workspaces/$(AML_WORKSPACE_NAME)

tf-import-adls:
	terraform import -var-file="${TF_VAR_FILE_PATH}" azurerm_storage_account.default /subscriptions/$(ARM_SUBSCRIPTION_ID)/resourceGroups/$(AML_RESOURCE_GROUP)/providers/Microsoft.Storage/storageAccounts/$(ADLS_ACCOUNT_NAME)

tf-fmt-check:
	terraform fmt -check

tf-plan:
	terraform plan -input=false -out "../env/${TF_WORKSPACE}/${TF_OUTPUT_NAME}"

tf-plan-no-output:
	terraform plan -input=false

tf-plan-destroy:
	terraform plan -destroy -input=false -out="../env/${TF_WORKSPACE}/${TF_OUTPUT_NAME}"

tf-plan-destroy-no-output:
	terraform plan -destroy -input=false

tf-apply:
	terraform apply "../env/${TF_WORKSPACE}/${TF_OUTPUT_NAME}"

tf-apply-aa:
	terraform apply -auto-approve

tf-apply-aa-no-input:
	terraform apply -auto-approve -input=false

tf-destroy:
	terraform destroy

tf-destroy-aa:
	terraform destroy -auto-approve	
