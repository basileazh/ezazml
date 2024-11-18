# Installation

install-dependencies:
	${MAKE} -C ../.. install-dependencies

# Login

login:
	az account set -s $(ARM_SUBSCRIPTION_ID)
	az login

login-spn:
	az login --service-principal --tenant $(ARM_TENANT_ID) -u $(ARM_CLIENT_ID) -p $(ARM_CLIENT_SECRET)
	az account set -s $(ARM_SUBSCRIPTION_ID)

# Infrastructure as Code with Terraform

tf-init:
	${MAKE} -C ../../iac/ tf-init

tf-upgrade:
	${MAKE} -C ../../iac/ tf-upgrade

tf-import-rg:
	${MAKE} -C ../../iac/ tf-import-rg

tf-import-adls:
	${MAKE} -C ../../iac/ tf-import-adls

tf-plan-no-output-aa:
	${MAKE} -C ../../iac/ tf-plan-no-output-aa

tf-fmt-check:
	${MAKE} -C ../../iac/ tf-fmt-check

tf-plan:
	${MAKE} -C ../../iac/ tf-plan

tf-apply:
	${MAKE} -C ../../iac/ tf-apply

tf-apply-aa:
	${MAKE} -C ../../iac/ tf-apply-aa

tf-apply-aa-no-input:
	${MAKE} -C ../../iac/ tf-apply-aa-no-input

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

