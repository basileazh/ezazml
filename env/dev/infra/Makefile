.PHONY: tf-init tf-plan tf-apply login-spn tf-import-rg

login-spn:
	az login --service-principal --tenant $(AZURE_TENANT_ID) -u $(AZURE_CLIENT_ID) -p $(AZURE_CLIENT_SECRET)
	az account set -s $(AZURE_SUBSCRIPTION_ID)

tf-init:
	terraform init

tf-import-rg:
	terraform import -var-file="${TF_VAR_FILE_PATH}" azurerm_resource_group.default /subscriptions/$(AZURE_SUBSCRIPTION_ID)/resourceGroups/$(RG_NAME)

tf-plan:
	terraform plan -var-file "${TF_VAR_FILE_PATH}" -out "${TF_OUTPUT_PATH}"

tf-apply:
	terraform apply "dev.tfplan"