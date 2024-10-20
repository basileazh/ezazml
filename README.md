[//]: # (###### Description: This file contains the service for managing trips in the database.)

[//]: # (###### Created: 2024-05)

[//]: # (###### Created by: Basile El Azhari)

[//]: # (###### Maintained by: Basile El Azhari and Simon Hemi)

[//]: # (###### Contact: hitchhikesaver@gmail.com)

#   EZAZ ML : Easy Azure ML

[//]: # ([![Build Status]&#40;https://dev.azure.com/ezazml/ezazml/_apis/build/status/ezazml.ezazml?branchName=main&#41;]&#40;https://dev.azure.com/ezazml/ezazml/_build/latest?definitionId=1&branchName=main&#41;)
[//]: # ([![codecov]&#40;https://codecov.io/gh/ezazml/ezazml/branch/main/graph/badge.svg?token=JZQZQZQZQZ&#41;]&#40;https://codecov.io/gh/ezazml/ezazml&#41;)
[//]: # ([![PyPI version]&#40;https://badge.fury.io/py/ezazml.svg&#41;]&#40;https://badge.fury.io/py/ezazml&#41;)

[//]: # ([![PyPI - Downloads]&#40;https://img.shields.io/pypi/dm/ezazml&#41;]&#40;https://pypi.org/project/ezazml/&#41;)

[//]: # ([![PyPI - Python Version]&#40;https://img.shields.io/pypi/pyversions/ezazml&#41;]&#40;https://pypi.org/project/ezazml/&#41;)

[//]: # ([![PyPI - License]&#40;https://img.shields.io/pypi/l/ezazml&#41;]&#40;https://pypi.org/project/ezazml/&#41;)

[![Azure ML](https://img.shields.io/badge/Azure%20ML-SDK-blue)](https://pypi.org/project/azureml-sdk/)
[![Databricks](https://img.shields.io/badge/Databricks-SDK-blue)](https://pypi.org/project/databricks-cli/)
[![Azure Data Lake Storage](https://img.shields.io/badge/Azure%20Data%20Lake%20Storage-SDK-blue)](https://pypi.org/project/azure-storage-file-datalake/)
[![Azure Blob Storage](https://img.shields.io/badge/Azure%20Blob%20Storage-SDK-blue)](https://pypi.org/project/azure-storage-blob/)
[![Terrform](https://img.shields.io/badge/Terraform-SDK-blue)](https://pypi.org/project/terraform/)
[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/downloads/)

[//]: # ([![GitHub]&#40;https://img.shields.io/github/workflow/status/ezazml/ezazml/CI?label=CI&#41;]&#40;

[//]: # ([![GitHub]&#40;https://img.shields.io/github/license/ezazml/ezazml&#41;]&#40;https://github.com/basileazh/ezazml/blob/main/LICENSE&#41;)

[//]: # ([![GitHub]&#40;https://img.shields.io/github/issues/ezazml/ezazml&#41;]&#40;https://github.com/basileazh/ezazml/issues&#41;)

[//]: # ([![GitHub]&#40;https://img.shields.io/github/stars/ezazml/ezazml&#41;]&#40;https://github.com/basileazh/ezazml/stargazers&#41;)

[//]: # ([![GitHub]&#40;https://img.shields.io/github/forks/ezazml/ezazml&#41;]&#40;https://github.com/basileazh/ezazml/network/members&#41;)

[//]: # ([![GitHub]&#40;https://img.shields.io/github/contributors/ezazml/ezazml&#41;]&#40;https://github.com/basileazh/ezazml/graphs/contributors&#41;)



## Introduction

This repository is a solution with an IaC definition in Terraform, a CLI and configuration with environment variables to make it easy to use Azure ML. 
It is a simple way to ship production-ready Azure ML pipelines and models 
without having to worry about the complexity of the Azure ML SDK.

Using this package, you will be able to deploy a full MLOPS system before the end of your day, 
just by configuring environment variables. For the moment, the following use case is supported : 

![20240919_ezazml_documentation_simple_MLOPS_overview.jpg](docs%2Fv0%2F20240919_ezazml_documentation_simple_MLOPS_overview.jpg)


## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the [LICENSE](LICENSE) file for details.


## Installation

### Prerequisites

- Python >= 3.10  https://www.python.org/downloads/
- Poetry          https://python-poetry.org/docs/


### Installation

To install the package, you can run the following command:

```bash
pip install ezazml
```

Then, to retrieve the template project folder please set the following environment variables in the `.env` file
or export them in the terminal:

```dotenv
# Application settings
EZAZML_REPOSITORY_URL="https://github.com/basileazh/ezazml.git"
PROJECT_FOLDER_NAME=<project_folder_name>
```

And run the following command to retrieve the template project folder:

```bash
ezazml init 
````

The template project will de cloned from the `EZAZML_REPOSITORY_URL` in the `PROJECT_FOLDER_NAME` directory. You can then
navigate to the `env/dev/` folder and start configuring the rest of the environment variables.

Alternatively, you can clone the repository and navigate to the `env/dev/` folder to start configuring the 
environment variables using the following command:

```bash
git clone https://github.com/basileazh/ezazml.git
```

## Configuration

Configuring the application is done with environment variables.

You can configure using a `.env` file or by exporting the environment variables yourself.

Here is how to create a `.env` file in the `env/prd/` or `env/dev/` directory of your project and add the following environment variables:

```dotenv
# Application settings
EZAZML_REPOSITORY_URL="https://github.com/basileazh/ezazml.git"
PROJECT_FOLDER_NAME=<project_folder_name>

# Auth settings
ARM_CLIENT_ID=<spn_client_ID># Service Principal client ID for auth to Azure. Available in the Azure portal and after the first Terraform apply iac deployment.
ARM_CLIENT_SECRET=<spn_client_secret># Service Principal secret for auth to Azure. Available in the Azure portal and after the first Terraform apply iac deployment.
ARM_TENANT_ID=<tenant_ID># Tenant ID for auth to Azure. Available in the Azure portal.
ARM_SUBSCRIPTION_ID=<subscription_ID># Subscription ID for auth to Azure. Available in the Azure portal.

## Terraform
TF_OUTPUT_NAME=tf.tfplan
TF_WORKSPACE=<dev># Other workspaces can be created by duplicating the structure in the env/ folder.
## Resource group
TF_VAR_tenant_id==<tenant_ID># Same as ARM_TENANT_ID
TF_VAR_location=westeurope# The location of the to-be Azure resource. https://azure.microsoft.com/en-gb/explore/global-infrastructure/geographies/
TF_VAR_resource_name_prefix=<resource_name_prefix># The prefix for the to-be resource names. Ex: "ezazml"
## Authentication, users and spn
TF_VAR_super_user_object_id==<super_user_object_id># The object ID of the super user. Can be found in the Azure portal.
TF_VAR_auth_application_name_prefix=<auth_application_name># The full application name will be the concatenation of the auth_application_name and the workspace name
TF_VAR_user_principal_name_prefix=<user_principal_name_prefix># The full user principal name will be the concatenation of the user_principal_name, '@' and the domain of the tenant
TF_VAR_user_display_name=<user_display_name>
TF_VAR_user_password=user_password>
## Storage
TF_VAR_adls_container_name=<adls_container_name># The name of the to-be ADLS container. Ex: "ezazml"
## Compute
TF_VAR_compute_instance_size_dev="Standard_A1_v2"
TF_VAR_compute_cluster_size_dev="Standard_A1_v2"
TF_VAR_compute_cluster_size_prd="Standard_A1_v2"
TF_VAR_compute_instance_count_dev=0
TF_VAR_compute_instance_count_prd=0
TF_VAR_compute_cluster_count_dev=1
TF_VAR_compute_cluster_count_prd=1
TF_VAR_compute_cluster_priority_dev="LowPriority"# LowPriority or Dedicated
TF_VAR_compute_cluster_priority_prd="LowPriority"# LowPriority or Dedicated
TF_VAR_compute_cluster_scale_min_node_dev=0
TF_VAR_compute_cluster_scale_min_node_prd=0
TF_VAR_compute_cluster_scale_max_node_dev=3
TF_VAR_compute_cluster_scale_max_node_prd=3

# Azure ML settings
AML_WORKSPACE_NAME=<your_workspace_name># The name of the Azure ML workspace. Available in the Azure portal.
AML_RESOURCE_GROUP=<your_resource_group># The name of the Azure ML resource group. Available in the Azure portal.

# Data settings
DATA_PATH=<path_to_input_data># The path to the input data. Can be a local path, a URL, a path to a blob storage or a combination or list of these.
DATA_INPUTS_EXTENSION=<csv,parquet,json_or_delta>
DATA_MLTABLE_SAVE_PATH=<path_to_save_mltable># Recommended naming convention for the MLTable save path: data/bronze/ml_table_titanic
DATA_HEADERS=all_files_same_headers# Only for CSV. Other options are all_files_different_headers, from_first_file, no_header
DATA_DESCRIPTION='My feature dataframe asset'
DATA_INFER_COLUMN_TYPES_CSV=True# Only for CSV. Set to True to infer column types
DATA_INPUT_KEEP_COLUMNS=# Comma-separated list of columns to keep
DATA_INPUT_DROP_COLUMNS=# Comma-separated list of columns to drop

# ADLS settings - if you want to use ADLS as a storage
ADLS_ACTIVATE=True# Set to True to use ADLS as a storage.
ADLS_ACCOUNT_KEY=<set_your_account_key>
ABDS_NAME=<abds_name># The name of the to-be Azure Blob Datastore that will be created in the Azure ML workspace to access the ADLS container.
ABDS_DESCRIPTION='Datastore pointing to a blob container using https protocol. From the Azure ML workspace.'
ABDS_ACCOUNT_NAME=<set_your_account_name># The name of the ADLS account. Available in the Azure portal.
ABDS_CONTAINER_NAME=<set_your_container_name># The name of the ADLS container. Available in the Azure portal.
ABDS_PROTOCOL=https

# Databricks settings - if you want to use Databricks as a storage
DATABRICKS_ACTIVATE=<True_or_False># Set to True to use Databricks as a storage. Should be set to False if ADLS is used.
DATABRICKS_HOST=<your_host_url>
DATABRICKS_PAT=<your_token>
DATABRICKS_DBFS_PREFIX=dbfs://

# Model settings
MODEL_PATH=/models
MODEL_NAME=model.pkl
MODEL_VERSION=1.0
MODEL_VERSION_NOTE='First version of the model'
# ADD HERE ENV VARS FOR MODEL DEPLOYMENT AS AN ALWAYS-ON ENDPOINT

# Logging settings
# The log file path template should contain a [DATETIME_PLACEHOLDER] that will be replaced by the current datetime.
LOG_FILE_PATH_TEMPLATE=logs/[DATETIME_PLACEHOLDER]_app.log
LOG_FORMAT='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s'
LOG_DATETIME_FORMAT=%Y-%m-%d_%H
```

If you use dotenv, add `dotenv` before every following `make` command in the `env/dev/` or `env/prd/` to load the environment variables.


## Infrastructure as Code

Terraform Configuration Documentation for Azure ML Deployment

### Overview
This package provides a Terraform configuration to deploy an Azure Machine Learning (Azure ML) instance, along with other associated services on Azure. The infrastructure is designed to be modular and environment-specific, allowing for deployment in different environments like `dev`, `prd`, etc.

### Prerequisites
Before deploying the infrastructure, ensure you have the following prerequisites:
- Azure Subscription 
https://azure.microsoft.com/en-us/free/
- Azure CLI           
https://docs.microsoft.com/en-us/cli/azure/install-azure-cli
- Terraform CLI       
https://learn.hashicorp.com/tutorials/terraform/install-cli
- Azure Data Lake Storage (ADLS) account dedicated to terraform backend management across projects
  (if backend is configured to use ADLS)
https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction
- Environment variables set in the `.env` file or exported in the terminal

### Terraform Backend Configuration

The Terraform backend is configured to use Azure Data Lake Storage (ADLS) as the backend storage.
To configure the backend, open the `iac/providers.tf` file and set the following variables:
```hcl
  backend "azurerm" {
    resource_group_name  = "terraform-state-rg"
    storage_account_name = "terraformbackendasa"
    container_name       = "tfstate"
    key                  = "terraform.tfstate"
  }
```

### Services Defined in Terraform Code
The Terraform configuration in this package deploys the following services:
- Azure Machine Learning Instance
- 1 Resource Group containing all resources
- 1 Storage Account with Blob Container
- 1 Application and Service Principal
- 1 User registered in Azure AD and to the application
- 1 Key Vault with 2 secrets
  - 1 for the application client_id
  - 1 for the application password
- 1 Container Registry
- 1 Application Insights

  
### Instructions for Deployment

#### Step 1: Navigate to the Environment Folder

To begin the deployment, navigate to the environment folder corresponding to the environment you wish to deploy 
(e.g., `env/dev/` for development). You can create other environments by duplicating the structure in the `env/` folder.
All Terraform commands must be run from within the selected environment folder if you have stored your environment 
variables in a `.env` file there.

#### Step 2: Set Environment Variables

Set the following environment variables in the `.env` file or export them in the terminal.
`ARM_TENANT_ID`, `ARM_SUBSCRIPTION_ID` are available in the Azure portal. All other variables can be set according
to your requirements. See the previous section for a detailed explanation of each variable. 
```dotenv
# Infrastructure settings
## Terraform
TF_OUTPUT_NAME: "tf.tfplan"
TF_WORKSPACE: "dev"
## Resource group
TF_VAR_tenant_id: ${{ secrets.TF_VAR_TENANT_ID }}
TF_VAR_location: "westeurope"
TF_VAR_resource_name_prefix: "ezazml"
## Authentication, users and spn
TF_VAR_super_user_object_id: ${{ secrets.TF_VAR_SUPER_USER_OBJECT_ID }}
TF_VAR_auth_application_name_prefix: "ezazml-app"
TF_VAR_user_principal_name_prefix: "user1"
TF_VAR_user_display_name: "User 1"
TF_VAR_user_password: ${{ secrets.TF_VAR_USER_PASSWORD }}
## Storage
TF_VAR_adls_container_name: "ezazml"
## Compute
TF_VAR_compute_instance_size_dev: "Standard_A1_v2"
TF_VAR_compute_cluster_size_dev: "STANDARD_DS2_V2"
TF_VAR_compute_cluster_size_prd: "Standard_A1_v2"
TF_VAR_compute_instance_count_dev: "0"
TF_VAR_compute_instance_count_prd: "0"
TF_VAR_compute_cluster_count_dev: "1"
TF_VAR_compute_cluster_count_prd: "1"
TF_VAR_compute_cluster_priority_dev: "Dedicated"
TF_VAR_compute_cluster_priority_prd: "LowPriority"
TF_VAR_compute_cluster_scale_min_node_dev: "0"
TF_VAR_compute_cluster_scale_min_node_prd: "0"
TF_VAR_compute_cluster_scale_max_node_dev: "3"
TF_VAR_compute_cluster_scale_max_node_prd: "3"
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
```dotenv
ARM_CLIENT_ID=<your_azure_client_id>
ARM_CLIENT_SECRET=<your_azure_client_secret>
```
If you retrieved the service principal credentials from a previous deployment, you can set them as environment variables 
with a Contributor role by default on the Resource group containing all resources including Azure ML workspace.

After setting the environment variables, authenticate to Azure using the service principal:
```bash
make login-spn
```

#### Step 4: Initialize Terraform

Run the following command to initialize Terraform. This will set up the backend and configure the state according 
to the settings in the `providers.tf` file. Additionally, the `dev` workspace will be created if it does not already exist.

```bash
make tf-init
``` 

**Note:** 
- If your backend is configured to use Azure Data Lake Storage (ADLS), you will need to create the storage account 
beforehand in a dedicated resource group.
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
```dotenv
ARM_CLIENT_ID=<your_azure_client_id>
ARM_CLIENT_SECRET=<your_azure_client_secret>
```

Azure portal: https://portal.azure.com/

### Conclusion on infrastructure deployment
This documentation provides the necessary steps to deploy Azure ML and associated services using Terraform. Ensure you have set all required environment variables, authenticate to Azure correctly, and follow the outlined steps for a successful deployment.


## Azure ML Workspace Management

This package provides the `ezazml` CLI command to interact with your Azure ML Workspace. 
We are going to set up the data assets and the model assets in the Azure ML Workspace. We are then going to deploy the 
model as an always-on endpoint or to be used in a batch inference pipeline.

### Overview

The `ezazml` CLI is a command-line interface that allows you to interact with your Azure ML Workspace.
It provides commands to create or update datastores, upload files to datastores, and create MLTables to 
reference your training datasets. It provides several default use cases to simplify the process of setting up 
your MLOPS Azure ML Workspace for training and inference jobs.

### Prerequisites

- Python >= 3.10  https://www.python.org/downloads/
- Poetry          https://python-poetry.org/docs/

### Installation

To install the package, navigate to the `env/dev/` folder of this repository and run the following command:

```bash
make install-dependencies
```

Please activate you virtualenv before running the commands. If you are using Poetry, it can be done with `poetry shell`
or by adding `poetry run` before any command.

You should then be able to run the `ezazml` command in your terminal.

```bash
ezazml --help
```

If you use a `.env` file, add `dotenv` before every following `make`, `poetry run` or any `ezazml` 
command in the `env/dev/` or `env/prd/` to load the environment variables. 
You can also export the environment variables in the terminal.

### 1. Data initialization and update

The following commands will create a `datastore` and a `mltable` objects in your Azure ML Workspace, making it ready 
for training and inference jobs.

#### 1.1 (Optional) Create or update Azure ML datastore (from an ADLS container)

If your data is stored on Azure Data Lake Storage (ADLS), you should create or update a datastore pointing to the 
ADLS container. 

Please set the following environment variables:

```dotenv
# ADLS settings - if you want to use ADLS as a storage
ADLS_ACTIVATE=True
ADLS_ACCOUNT_KEY=<set_your_accoug6nt_key>
ABDS_NAME=<abds_name>
ABDS_DESCRIPTION='Datastore pointing to a blob container using https protocol. From the Azure ML workspace.'
ABDS_ACCOUNT_NAME=<set_your_account_name>
ABDS_CONTAINER_NAME=<set_your_container_name>
ABDS_PROTOCOL=https
```

Then run the following command (prepend `dotenv` if you are using a `.env` file):

```bash
make create-or-update-adls-datastore
```

Alternatively, you can run the following command without setting the environment variables:

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

Please set the following environment variables:

```dotenv
# Azure ML settings
AML_WORKSPACE_NAME=<your_workspace_name># The name of the Azure ML workspace. Available in the Azure portal.
AML_RESOURCE_GROUP=<your_resource_group># The name of the Azure ML resource group. Available in the Azure portal.

# Data settings
DATA_PATH=<path_to_input_data># The path to the input data. Can be a local path, a URL, a path to a blob storage or a combination or list of these.
DATA_INPUTS_EXTENSION=<csv,parquet,json,delta>
DATA_MLTABLE_SAVE_PATH=<path_to_save_mltable>
DATA_HEADERS=all_files_same_headers# Only for CSV. Other options are all_files_different_headers, from_first_file, no_header
DATA_DESCRIPTION='My feature dataframe asset'
DATA_INFER_COLUMN_TYPES_CSV=True# Only for CSV. Set to True to infer column types
DATA_INPUT_KEEP_COLUMNS=# Comma-separated list of columns to keep
DATA_INPUT_DROP_COLUMNS=# Comma-separated list of columns to drop

# Databricks settings - if you want to use Databricks as a storage
DATABRICKS_ACTIVATE=<True_or_False>
DATABRICKS_HOST=<your_host_url>
DATABRICKS_PAT=<your_token>
DATABRICKS_DBFS_PREFIX=dbfs://
```

**Notes:**
- The `DATA_PATH` can be a local path, a URL, a path to a blob storage or a combination or list of these. For example, 
you can set `DATA_PATH` to `"https://github.com/datasciencedojo/datasets/blob/master/titanic.csv"` to download the
Titanic dataset from GitHub. It is also possible to set `DATA_PATH` to a local path like `./data/titanic.csv` to use a
local file. Finally, you can set `DATA_PATH` to a combination of these, like 
`"./data/titanic_extra_data.csv,https://github.com/datasciencedojo/datasets/blob/master/titanic.csv"`.  
- the `--infer-column-types` flag is only available for CSV files. It will infer the column types of the dataset. 
To remove it, please go to the Makefile at the root of the repository and remove the `--infer-column-types` flag in the
`create-mltable` command.
- The `--include-path-column` flag is available to include the path column in the MLTable. To remove it, please go to the
Makefile at the root of the repository and remove the `--include-path-column` flag in the `create-mltable` command.
- The `--keep-columns` and `--drop-columns` options are available to keep or drop specific columns from the dataset. To avoid using them, 
don't set them or set their values to an empty string.

Then run the following command:
    
```bash
make create-mltable
```

Alternatively, you can run the following command without setting the environment variables:

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
- `LOG_FILE_PATH_TEMPLATE`  The path template to the log file  
- `LOG_FORMAT`              The log format
- `LOG_DATETIME_FORMAT`     The datetime format

## Deployment

Once you have deployed all resources in the dev environment and you are satisfied with your setup,
you can use this package in your CICD process for production deployment.
An example of CICD pipeline is provided in the XXXXXX folder

## Development

To contribute to this project, you can follow the following steps:

1. Clone the repository
2. Create a new branch
3. Make your changes
4. Run the tests
5. Create a pull request
6. Wait for the review
7. Merge the pull request
8. Celebrate

### Run tests

Here are the commands to run the package tests, and clean the integration tests outputs. They will ensure that all 
operations run correctly. We recommend running them, then destroying the infrastructure and redeploying it to ensure 
that the state is clean.

```bash
make run-tests
make run-tests-cov
make clean-tests-files
```

## TODO

### Priority level 1 - HOT
Bug fixes, critical improvements, current sprint tasks.

-  Training
  - Add a command to train a model in the Azure ML workspace.
  - Add a command to register the model in the Azure ML workspace.
  - Add a command to deploy the model as an always-on endpoint in the Azure ML workspace.
  - Add a command to deploy the model in a batch inference pipeline in the Azure ML workspace.

### Priority level 2 - WARM
Medium issues, improvements, next sprint tasks.

- Inference
  - Add a command to run a batch inference pipeline in the Azure ML workspace.
  - Add a command to run a batch inference pipeline in the Azure ML workspace with a model registered in the workspace.

- Monitoring
  - Add a command to set the monitoring configuration in the Azure ML workspace.
  - Add a command to retrieve the monitoring logs of the Azure ML workspace.
  - 
### Priority level 3 - COLD
Minor issues that can be fixed later, minor improvements, refactoring.

- Documentation
  - Add a section in the README.md file to explain how to deploy the package in a CICD pipeline.

- Tests
  - Repair tests in `tests/services/test_ml_client.py` and `tests/services/data/test_data.py`. 
  Most issues seems to come from a bad use of mocking.

- Terraform
  - Add the `env/prd/` folder and the `make tf-init` command to initialize the production workspace.
  - Some values are hardcoded in the Terraform code. They should be set as variables in the `variables.tf` file 
  and declared as environment variables `TF_VAR_xxx` in the template `.env` file in the `README.md` file.