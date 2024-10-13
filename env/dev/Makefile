# Installation

install-dependencies:
	${MAKE} -C ../.. install-dependencies

# Login

login:
	az login
	az account set -s $(AZURE_SUBSCRIPTION_ID)

login-spn:
	az login --service-principal --tenant $(AZURE_TENANT_ID) -u $(AZURE_CLIENT_ID) -p $(AZURE_CLIENT_SECRET)
	az account set -s $(AZURE_SUBSCRIPTION_ID)

# Infrastructure as Code with Terraform

tf-init:
	${MAKE} -C ../../iac/ tf-init

tf-upgrade:
	${MAKE} -C ../../iac/ tf-upgrade

tf-import-rg:
	${MAKE} -C ../../iac/ tf-import-rg

tf-plan:
	${MAKE} -C ../../iac/ tf-plan

tf-apply:
	${MAKE} -C ../../iac/ tf-apply

tf-apply-aa:
	${MAKE} -C ../../iac/ tf-apply-aa

tf-destroy:
	${MAKE} -C ../../iac/ tf-destroy

tf-destroy-aa:
	${MAKE} -C ../../iac/ tf-destroy-aa

# Azure ML Workspace Setup

create-or-update-adls-datastore:
	${MAKE} -C ../../ create-or-update-adls-datastore

create-mltable:
	${MAKE} -C ../../ create-mltable

# Development

run-tests:
	${MAKE} -C ../../ run-tests

run-tests-cov:
	${MAKE} -C ../../ run-tests-cov

clean-tests-files:
	${MAKE} -C ../../ clean-tests-files

clean-pycache:
	${MAKE} -C ../../ clean-pycache

