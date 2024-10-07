install-dependencies:
	${MAKE} -C ../.. install-dependencies

login:
	az login
	az account set -s $(AZURE_SUBSCRIPTION_ID)

login-spn:
	az login --service-principal --tenant $(AZURE_TENANT_ID) -u $(AZURE_CLIENT_ID) -p $(AZURE_CLIENT_SECRET)
	az account set -s $(AZURE_SUBSCRIPTION_ID)

run-tests:
	${MAKE} -C ../../ run-tests

run-tests-cov:
	${MAKE} -C ../../ run-tests-cov

tf-init:
	${MAKE} -C infra/ tf-init

tf-upgrade:
	${MAKE} -C infra/ tf-upgrade

tf-import-rg:
	${MAKE} -C infra/ tf-import-rg

tf-plan:
	${MAKE} -C infra/ tf-plan

tf-apply:
	${MAKE} -C infra/ tf-apply

tf-apply-aa:
	${MAKE} -C infra/ tf-apply-aa