# EZAZ ML : Easy Azure ML

[//]: # ([![Build Status]&#40;https://dev.azure.com/ezazml/ezazml/_apis/build/status/ezazml.ezazml?branchName=main&#41;]&#40;https://dev.azure.com/ezazml/ezazml/_build/latest?definitionId=1&branchName=main&#41;)
[//]: # ([![codecov]&#40;https://codecov.io/gh/ezazml/ezazml/branch/main/graph/badge.svg?token=JZQZQZQZQZ&#41;]&#40;https://codecov.io/gh/ezazml/ezazml&#41;)
[![PyPI version](https://badge.fury.io/py/ezazml.svg)](https://badge.fury.io/py/ezazml)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/ezazml)](https://pypi.org/project/ezazml/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ezazml)](https://pypi.org/project/ezazml/)
[![PyPI - License](https://img.shields.io/pypi/l/ezazml)](https://pypi.org/project/ezazml/)

[![Azure ML](https://img.shields.io/badge/Azure%20ML-SDK-blue)](https://pypi.org/project/azureml-sdk/)
[![Databricks](https://img.shields.io/badge/Databricks-SDK-blue)](https://pypi.org/project/databricks-cli/)
[![Azure Data Lake Storage](https://img.shields.io/badge/Azure%20Data%20Lake%20Storage-SDK-blue)](https://pypi.org/project/azure-storage-file-datalake/)
[![Azure Blob Storage](https://img.shields.io/badge/Azure%20Blob%20Storage-SDK-blue)](https://pypi.org/project/azure-storage-blob/)

[![GitHub](https://img.shields.io/github/license/ezazml/ezazml)](


## Introduction

This repository is a solution with an IaC definition in Terraform, a CLI and configuration with environment variables to make it easy to use Azure ML. 
It is a simple way to ship production-ready Azure ML pipelines and models 
without having to worry about the complexity of the Azure ML SDK.

Using this package, you will be able to deploy a full MLOPS system before the end of your day, 
just by configuring environment variables. For the moment, the following use case is supported : 

![20240919_ezazml_documentation_simple_MLOPS_overview.jpg](docs%2Fv0%2F20240919_ezazml_documentation_simple_MLOPS_overview.jpg)


## Configuration

Configuring the application is done with environment variables.

You can configure using a `.env` file or by exporting the environment variables yourself.

Here is how to create a `.env` file in the `env/prd/` or `env/dev/` directory of your project and add the following environment variables:

```dotenv
# Auth settings
AZURE_CLIENT_ID=<spn_client_ID>
AZURE_CLIENT_SECRET=<spn_client_secret>
AZURE_TENANT_ID=<tenant_ID>
AZURE_SUBSCRIPTION_ID=<subscription_ID>

# Infrastructure settings
TF_WORKSPACE=<dev_or_prd>
TF_VAR_backend_resource_name=<ex_terraform-state-rg>
TF_VAR_backend_storage_account_name=<ex_terraformbackendasa>
TF_VAR_backend_container_name=<ex_tfstate>
TF_VAR_backend_terraform_state_key=<ex_terraform.tfstate>
TF_VAR_super_user_object_id=<superuser_object_id>
TF_VAR_tenant_id=<tenant_ID>
TF_VAR_auth_application_name_prefix=<auth_application_name>
# The full application name is the concatenation of the auth_application_name and the workspace name
TF_VAR_user_principal_name_prefix=<user_principal_name_prefix>
TF_VAR_user_display_name=<user_display_name>
TF_VAR_user_password=<user_password>
TF_VAR_location=westeurope
TF_VAR_resource_name_prefix=<resource_name_prefix>
TF_OUTPUT_NAME=tf.tfplan



# Azure ML settings
AML_WORKSPACE_NAME=<your_workspace_name>
AML_RESOURCE_GROUP=<your_resource_group>

# Model settings
MODEL_PATH=/models
MODEL_NAME=model.pkl
MODEL_VERSION=1.0
MODEL_VERSION_NOTE='First version of the model'
# ADD HERE ENV VARS FOR MODEL DEPLOYMENT AS AN ALWAYS-ON ENDPOINT

# Data settings
DATA_PATH=
DATA_MLTABLE_SAVE_PATH=
DATA_INPUT_EXTENSION=
DATA_HEADERS=
DATA_DESCRIPTION='My feature dataframe asset'

# ADLS settings - if you want to use ADLS as a storage
ADLS_ACTIVATE=True
ADLS_ACCOUNT_KEY=<set_your_account_key>
ABDS_NAME=<abds_name>
ABDS_DESCRIPTION='Datastore pointing to a blob container using https protocol. From the Azure ML workspace.'
ABDS_ACCOUNT_NAME=<set_your_account_name>
ABDS_CONTAINER_NAME=<set_your_container_name>
ABDS_PROTOCOL=https

# Databricks settings - if you want to use Databricks as a storage
DATABRICKS_ACTIVATE=False
DATABRICKS_HOST=<your_host_url>
DATABRICKS_PAT=<your_token>
DATABRICKS_DBFS_PREFIX=dbfs://

# Logging settings
LOG_FILE_PATH_TEMPLATE=logs/[DATETIME_PLACEHOLDER]_app.log
LOG_FORMAT='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s'
LOG_DATETIME_FORMAT=%Y-%m-%d_%H

# Adjust the LOG_FILE_PATH according to your environment
LOG_FILE_PATH=logs/[DATETIME_PLACEHOLDER]_app.log
```

If you use dotenv, add `dotenv` before every following `make` command in the `env/dev/` or `env/prd/` to load the environment variables.


## Infrastructure as Code

Terraform Configuration Documentation for Azure ML Deployment

### Overview
This package provides a Terraform configuration to deploy an Azure Machine Learning (Azure ML) instance, along with other associated services on Azure. The infrastructure is designed to be modular and environment-specific, allowing for deployment in different environments like `dev`, `prd`, etc.

### Services Defined in Terraform Code
The Terraform configuration in this package deploys the following services:
- Azure Machine Learning Instance
- Resource Group(s)
- Storage Account (if backend is configured to use ADLS)
- Networking Components (if applicable)
- Azure Active Directory Integration (for authentication)
- Service Principal
- Other necessary services for Azure ML operations

### Instructions for Deployment

#### Step 1: Navigate to the Environment Folder

To begin the deployment, navigate to the environment folder corresponding to the environment you wish to deploy 
(e.g., `env/dev/` for development). You can create other environments by duplicating the structure in the `env/` folder.
All Terraform commands must be run from within the selected environment folder if you have stored your environment 
variables in a `.env` file there.

#### Step 2: Set Environment Variables

Set the following environment variables:
```bash
export AZURE_TENANT_ID=<your_azure_tenant_id>
export AZURE_SUBSCRIPTION_ID=<your_azure_subscription_id>
export TF_WORKSPACE=<terraform_workspace>
export TF_VAR_super_user_object_id=<super_user_object_id>
export TF_VAR_tenant_id=<tenant_id>
export TF_VAR_auth_application_name_prefix=<application_name_prefix>
export TF_VAR_user_principal_name_prefix=<user_principal_name_prefix>
export TF_VAR_user_display_name=<user_display_name>
export TF_VAR_user_password=<user_password>
export TF_VAR_location=<location>
export TF_VAR_resource_name_prefix=<resource_name_prefix>
export TF_OUTPUT_PATH=<path_to_store_terraform_output>
```
If you are using a `.env` file, ensure that the file is present in the environment folder and contains the required 
environment variables and set their values accordingly. 

#### Step 3: Authenticate to Azure

To authenticate to Azure, you have two options:

- **Using Personal Account:**
Run the following command to log in with your personal account, which is recommended for the first deployment:
```bash
make login
```

- **Using Service Principal:**
If you are logging in using a service principal, make sure to set the following environment variables:
```bash
- export AZURE_CLIENT_ID=<your_azure_client_id>
- export AZURE_CLIENT_SECRET=<your_azure_client_secret>
```
If you retrieved the service principal credentials from a previous deployment, you can set them as environment variables 
with a Contributor role by default on the Resource group containing all resources including Azure ML workspace.

After setting the environment variables, authenticate to Azure using the service principal:
```bash
make login-spn
```

#### Step 4: Initialize Terraform

Run the `make tf-init` command to initialize Terraform. This will set up the backend and configure the state according to the settings in the `providers.tf` file. Additionally, two workspaces, `dev` and `prd`, will be created.
**Note:** 
- If your backend is configured to use Azure Data Lake Storage (ADLS), you will need to create the storage account beforehand in a dedicated resource group.
- The recommended naming conventions for this Terraform setup can be found in the `infra/providers.tf` file.

#### Step 5: Import Existing Resource Group (Optional)

If you are deploying Azure ML into an existing resource group, you can import the resource group using the following command:
```bash
make tf-import-rg
```
#### Step 6: Review Changes
Before applying changes, run the `make tf-plan` command to review the changes that will be made:
```bash
make tf-plan
```
#### Step 7: Apply Changes
To apply the changes and create or update resources, run the following command:
```bash
make tf-apply
```

**SPN Credentials**
You can now retrieve the value of the authentication application name and the workspace name from the Terraform output.
You can use them to authenticate to Azure ML and interact with the workspace using the `ezazml` CLI, 
with a Contributor role by default on the Resource group containing all resources including Azure ML workspace.
```bash
- export AZURE_CLIENT_ID=<your_azure_client_id>
- export AZURE_CLIENT_SECRET=<your_azure_client_secret>
```

Azure portal: https://portal.azure.com/

### Conclusion on infrastructure deployment
This documentation provides the necessary steps to deploy Azure ML and associated services using Terraform. Ensure you have set all required environment variables, authenticate to Azure correctly, and follow the outlined steps for a successful deployment.


## Azure ML Workspace

This package provides the `ezazml` command to interact with your Azure ML Workspace. 
Please activate you virtualenv before running the commands. If you are using Poetry, it can be done with `poetry shell`
or by adding `poetry run` before any command.

```bash
ezazml --help
```

### 1. Data initialization and update

The following commands will create a `datastore` and a `mltable` objects in your Azure ML Workspace, making it ready for training and inference jobs.

#### 1.1 Create or update Azure ML datastore (from an ADLS container)
```bash
ezazml create-or-update-adls-datastore
```

#### 1.2  (Optional) Upload your training dataset to the datastore

If your training data is on your local environment, the following command will upload the dataset to the datastore:

```bash
ezazml upload-file-to-datastore <source_path> <dest_path_in_datastore> \
  --asset_type <uri_file, uri_folder or mltable> \
  --overwrite <overwrite, append or fail_on_file_conflict>
```

#### 1.3 Create a MLTable to reference your training dataset

A MLTable is a versioned Data Asset registered in Azure ML, enabling reproducibility, lineage and tracking.

```bash
ezazml create-mltable <source_path_1> <source_path_n> <save_path> \ 
  --inputs-extension=<csv, parquet, json or delta> \ 
  --data-description "My favourite input data" \
  --headers=all_files_same_headers \  # only for csv
  --infer-column-types \  # only for csv
  --include-path-column \  # is a flag, remove it not to include the path column
  --keep-columns <list of columns to keep, defaults to all> \
  --drop-columns <list of columns to drop, defaults to none>
```

An additional `--data-version` flag is available but its use is not recommended, as the version automatically increments.

Here is an example with actual data :

```bash
ezazml create-mltable wasbs://data@azuremlexampledata.blob.core.windows.net/titanic.csv raw/titanic_mlt \
  --inputs-extension=csv \
  --headers=all_files_same_headers \
  --infer-column-types \
  --include-path-column \
  --keep-columns=col1,col2 \
  --drop-columns=col3
```

### Logging

The logging configuration is set in the `.env` file with the following environment variables:
- `LOG_FILE_PATH`           The path to the log file
- `LOG_FILE_PATH_TEMPLATE`  The path template to the log file  
- `LOG_FORMAT`              The log format
- `LOG_DATETIME_FORMAT`     The datetime format

## Deployment

The best way to use this package is to use it in your CICD process.
An example of CICD pipeline is provided in the XXXXXX folder
TODO: Add CICD example and describe here how to build one's. Using a public Docker image (from this repo) ? Using commands ? 

## Development

### Prerequisites

- Python 3.10
- Poetry

### Installation

To install the package in development mode, navigate to the env/dev folder and run the following command:

```bash
make install-dependencies
```

### Usage

After installing the package, you have to set the environment variables in the `env/dev/.env` file or in the terminal.
If you use dotenv, add `dotenv` before every following `make` command to load the environment variables.

Please navigate to the `env/dev` folder and run the following command:

#### Initialize the Azure ML dev workspace

The `env/dev/init_ws.sh` gives you an example of script to initialize the data assets of your workspace.
Please change it the way it fits for your training dataset

#### Run tests

Here are the commands to run the tests, and clean the integration tests outputs:
```bash
make run-tests
make run-tests-cov
make clean-tests-files
```