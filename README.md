[//]: # (###### Description: This file contains the service for managing trips in the database.)

[//]: # (###### Created: 2024-05)

[//]: # (###### Created by: Basile El Azhari)

[//]: # (###### Maintained by: Basile El Azhari and Simon Hemi)

[//]: # (###### Contact: hitchhikesaver@gmail.com)

# EZAZ ML: Streamlined MLOps on Azure

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

[//]: # ([![GitHub]&#40;https://img.shields.io/github/workflow/status/ezazml/ezazml/CI?label=CI&#41;]&#40;)

[//]: # ([![GitHub]&#40;https://img.shields.io/github/license/ezazml/ezazml&#41;]&#40;https://github.com/basileazh/ezazml/blob/main/LICENSE&#41;)

[//]: # ([![GitHub]&#40;https://img.shields.io/github/issues/ezazml/ezazml&#41;]&#40;https://github.com/basileazh/ezazml/issues&#41;)

[//]: # ([![GitHub]&#40;https://img.shields.io/github/stars/ezazml/ezazml&#41;]&#40;https://github.com/basileazh/ezazml/stargazers&#41;)

[//]: # ([![GitHub]&#40;https://img.shields.io/github/forks/ezazml/ezazml&#41;]&#40;https://github.com/basileazh/ezazml/network/members&#41;)

[//]: # ([![GitHub]&#40;https://img.shields.io/github/contributors/ezazml/ezazml&#41;]&#40;https://github.com/basileazh/ezazml/graphs/contributors&#41;)


EZAZ ML is an end-to-end solution that dramatically simplifies the deployment and management of Machine Learning Operations on Azure. By combining Infrastructure as Code (Terraform), a powerful CLI, and environment-based configuration, it eliminates the complexity typically associated with Azure ML implementations.

All you need is a GitHub repository and an Azure Subscription, and you can have a fully functional MLOps environment in minutes. You can then customize it to your needs by setting the environment variables and updating the train.py and inference.py files.

## Agenda
1. [Why EZAZ ML?](#why-ezaz-ml)
2. [Current Capabilities](#current-capabilities)
3. [License](#license)
4. [Installation](#installation)
   - [Prerequisites](#prerequisites)
   - [Installation Steps](#installation)
   - [Configuration](#configuration)
5. [Infrastructure as Code](#infrastructure-as-code)
6. [Azure ML Workspace Management](#azure-ml-workspace-management)
7. [Deployment](#deployment)
8. [Development](#development)
9. [TODO](#todo)

## Why EZAZ ML?

- **Deploy in Minutes, Not Weeks**: Set up a complete MLOps environment on Azure ML in a single day through simple environment variable configuration
- **Production-Ready**: Includes best practices for security, scalability, and maintainability out of the box
- **Simplified Management**: Easy-to-use CLI for managing data assets, models, and deployments without deep Azure ML SDK knowledge
- **Easy to Customize**: Easily extendable to support additional features and integrations
- **Secure**: Built with security in mind, with best practices for RBAC, authentication and authorization

And Open Source obviously 🙂

## Current Capabilities

The package currently supports the following MLOps workflow:

<!-- ![20240919_ezazml_documentation_simple_MLOPS_overview.jpg](docs%2Fv0%2F20240919_ezazml_documentation_simple_MLOPS_overview.jpg) -->

Perfect for teams looking to:
- Quickly set up ML infrastructure on Azure, have a first model running in minutes
- Implement MLOps best practices without extensive cloud expertise
- Automate model training and deployment workflows
- Maintain consistent environments across development and production


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
```

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
# For the Project SPN
#ARM_CLIENT_ID=<project_spn_client_ID># Project SPN client ID. Available in the Azure portal.
# For the DevOPS SPN
ARM_CLIENT_ID=<devops_spn_client_ID># DevOPS SPN client ID. Available in the Azure portal.
# For the Project SPN
#ARM_CLIENT_SECRET=<project_spn_client_secret># Project SPN client secret. Available in the Azure portal.
# For the DevOPS SPN
ARM_CLIENT_SECRET=<devops_spn_client_secret># DevOPS SPN client secret. Available in the Azure portal.
ARM_TENANT_ID=<tenant_ID># Tenant ID for auth to Azure. Available in the Azure portal.
ARM_SUBSCRIPTION_ID=<subscription_ID># Subscription ID for auth to Azure. Available in the Azure portal.

## Terraform
TF_OUTPUT_NAME=tf.tfplan
TF_WORKSPACE=<dev># Other workspaces can be created by duplicating the structure in the env/ folder.
## Resource group
TF_VAR_tenant_id=<tenant_ID># Same as ARM_TENANT_ID
TF_VAR_location=westeurope# The location of the to-be Azure resource. https://azure.microsoft.com/en-gb/explore/global-infrastructure/geographies/
TF_VAR_resource_name_prefix=<resource_name_prefix># The prefix for the to-be resource names. Ex: "ezazml"
## Authentication, users and spn
TF_VAR_devops_spn_object_id==<devops_spn_object_id># The object ID (not client ID) of the DevOPS SPN. Can be found in the Azure portal.
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

### Auth settings & SPNs

The following block:
```dotenv
# Auth settings
# For the Project SPN
#ARM_CLIENT_ID=<project_spn_client_ID># Project SPN client ID. Available in the Azure portal.
# For the DevOPS SPN
ARM_CLIENT_ID=<devops_spn_client_ID># DevOPS SPN client ID. Available in the Azure portal.
# For the Project SPN
#ARM_CLIENT_SECRET=<project_spn_client_secret># Project SPN client secret. Available in the Azure portal.
# For the DevOPS SPN
ARM_CLIENT_SECRET=<devops_spn_client_secret># DevOPS SPN client secret. Available in the Azure portal.
```

enables you to use either the Project SPN or the DevOPS SPN. Here is when to use them:

- **DevOPS SPN**: Use it for Terraform deployments when making changes to the infrastructure. Tailored for DevOps with `Contributor` role on the Subscription.
- **Project SPN**: Use it for Docker image builds and deployments in your MLOPS pipelines, as well as for logging in to Azure Machine Learning Studio, reaching out to the Storage Account, etc. Tailored for the project with `Contributor` role on the Resource Group containing all resources.



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

### DevOPS Application SPN

To deploy the infrastructure, you will need to create a DevOPS Application associated with a Service Principal (SPN) in Azure. The DevOPS SPN will be used to authenticate to Azure and deploy the resources using Terraform.
The application should have the `Contributor` and `Role Based Access Control Administrator` roles on the Subscription, 
and be granted the following API permissions in Entra ID : 
- `Application.ReadWrite.OwnedBy`
- `Application.ReadWrite.All`
- `Directory.Read.All`
- `User.Read`
- `User.ReadWrite.All`

deployment and that will have the `Contributor` role on the Resource group containing all resources including 
Azure ML workspace. This allows us to restrict the permissions of the SPN to the 
scope of the Azure ML workspace. This can be done by following instructions at this page : 
https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/service_principal_client_secret


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
- Machine Learning Workspace
- Resource Group containing all resources
- Storage Account with Blob Container
- Application and Service Principal
- User registered in Azure AD and to the application
- Key Vault with 2 secrets
  - application (SPN) client_id
  - application (SPN) password
- Container Registry
- Application Insights

  
### Instructions for Deployment

The recommended way to deploy the infrastructure is to use GitHub Actions.

#### GitHub Actions Deployment

##### GHA Step 1: Configure GitHub Secrets
   Add the following secrets in your repository (Settings → Secrets and variables → Actions):
   ```text
   # Azure Authentication
   AZURE_CLIENT_ID          # DevOps SPN Client ID
   AZURE_SUBSCRIPTION_ID    # Azure Subscription ID
   AZURE_TENANT_ID         # Azure Tenant ID
   ARM_SUBSCRIPTION_ID     # Azure Subscription ID
   
   # Terraform Variables
   TF_VAR_DEVOPS_SPN_OBJECT_ID           # Object ID of the DevOps SPN
   TF_VAR_TF_BACKEND_STORAGE_ACCOUNT_ID   # Storage Account ID for Terraform backend
   TF_VAR_USER_PASSWORD                   # Password for the Azure AD user
   ```

##### GHA Step 2: Configure Environment Variables
   Review and modify environment variables in the workflow files as needed:
   ```yaml
   env:
     TF_WORKSPACE: "dev"
     TF_VAR_location: "westeurope"
     TF_VAR_resource_name_prefix: "ezazml"
     # ... other variables
   ```

##### GHA Step 3: Deploy Infrastructure
   - Push changes to `main` branch (affecting `.tf` files), or
   - Create a pull request, or
   - Manually trigger:
     1. Go to Actions → deploy_infra_terraform
     2. Click "Run workflow"
     3. Select branch
     4. Click "Run workflow"

##### GHA Step 4: Monitor Deployment
   - View progress in GitHub Actions tab
   - Check job outputs for each step
   - Review Terraform plans in job artifacts


#### CLI Deployment

Alternatively, you can follow the following instructions to deploy the infrastructure manually or using a CI/CD pipeline via CLI.

##### CLI Step 1: Navigate to the Environment Folder

To begin the deployment, navigate to the environment folder corresponding to the environment you wish to deploy 
(e.g., `env/dev/` for development). You can create other environments by duplicating the structure in the `env/` folder.
All Terraform commands must be run from within the selected environment folder if you have stored your environment 
variables in a `.env` file there.

##### CLI Step 2: Set Environment Variables

Set the following environment variables in the `.env` file or export them in the terminal.
`ARM_TENANT_ID`, `ARM_SUBSCRIPTION_ID` are available in the Azure portal. All other variables can be set according
to your requirements. See the previous section for a detailed explanation of each variable. 

```dotenv
# Auth settings
ARM_CLIENT_ID=<devops_spn_client_ID>
ARM_CLIENT_SECRET=<devops_spn_client_secret>
ARM_TENANT_ID=<tenant_ID>
ARM_SUBSCRIPTION_ID=<subscription_ID>

# Infrastructure settings
## Terraform
TF_OUTPUT_NAME: "tf.tfplan"
TF_WORKSPACE: "dev"
## Resource group
TF_VAR_tenant_id=<tenant_ID>
TF_VAR_location="westeurope"
TF_VAR_resource_name_prefix="ezazml"
## Authentication, users and spn
TF_VAR_devops_spn_object_id=<devops_spn_object_id>
TF_VAR_tf_backend_storage_account_id=<tf_backend_storage_account_id>
TF_VAR_auth_application_name_prefix="ezazml-app"
TF_VAR_user_principal_name_prefix="user1"
TF_VAR_user_display_name="User 1"
TF_VAR_user_password=<user_password>
## Storage
TF_VAR_adls_container_name="ezazml"
## Compute
TF_VAR_compute_instance_size_dev="Standard_A1_v2"
TF_VAR_compute_cluster_size_dev="STANDARD_DS2_V2"
TF_VAR_compute_cluster_size_prd="Standard_A1_v2"
TF_VAR_compute_instance_count_dev="0"
TF_VAR_compute_instance_count_prd="0"
TF_VAR_compute_cluster_count_dev="1"
TF_VAR_compute_cluster_count_prd="1"
TF_VAR_compute_cluster_priority_dev="Dedicated"
TF_VAR_compute_cluster_priority_prd="LowPriority"
TF_VAR_compute_cluster_scale_min_node_dev="0"
TF_VAR_compute_cluster_scale_min_node_prd="0"
TF_VAR_compute_cluster_scale_max_node_dev="3"
TF_VAR_compute_cluster_scale_max_node_prd="3"
```
If you are using a `.env` file, ensure that the file is present in the environment folder and contains the required 
environment variables and set their values accordingly. 

##### CLI Step 3: Authenticate to Azure

To authenticate to Azure, you have two options:

- **Using Service Principal:**
This option is recommended for CICD pipelines and production deployments. You should provide a DevOPS Application with the `Contributor` and `Role Based Access Control Administrator` roles on the Subscription. Please refer to the [DevOPS Application SPN section](#devops-application-spn-section) for more details.  
If you are logging in using a service principal, make sure to set the following environment variables:
```dotenv
ARM_CLIENT_ID=<devops_spn_client_ID>
ARM_CLIENT_SECRET=<devops_spn_client_secret>
ARM_TENANT_ID=<tenant_ID>
ARM_SUBSCRIPTION_ID=<subscription_ID>
```

- **Using Personal Account:**

This option is available for development and testing purposes if your personal account benefits from at least the permissions needed for the [DevOPS Application SPN section](#devops-application-spn-section)
Run the following command to log in with your personal account, which is recommended for the first deployment:
```bash
make login
```


##### CLI Step 4: Initialize Terraform

Run the following command to initialize Terraform. This will set up the backend and configure the state according 
to the settings in the `providers.tf` file. Additionally, the `$TF_WORKSPACE` workspace will be created if it does not already exist, by default `dev`. 

The folder `env/<env_name>/` should have `<env_name> = $TF_WORKSPACE`. If the folder does not exist, you can create it by duplicating the structure of the `env/dev/` folder.

```bash
make tf-init
``` 

**Note:** 
- If your backend is configured to use Azure Data Lake Storage (ADLS), you will need to create the storage account 
beforehand in a dedicated resource group.
- The recommended naming conventions for this Terraform setup can be found in the `infra/providers.tf` file.

##### CLI Step 5: Import Existing Resource Group (Optional)
- If you have to create all resources, you can skip this step
- If you have to create all resources, in an Azure Subscription where you have deployed a project with different resources names you can skip this step
- If you are deploying Azure ML into an existing resource group, you can import the resource group using the following command:
```bash
make tf-import-rg
```
- If you recreate resources in the same Azure Subscription as a previous deployment that has been destroyed, and you want to keep the same resources names, you will have to manually purge from the Azure Portal:
  - Azure Key Vault
  - Azure ML Workspace
Open their respective resouce page, click on `Manage Deleted "resouce"` and Purge.

The Azure Data Lake Storage (ADLS) account cannot be destoryed, and then has to be restored and imported, otherwised to have its name changed. To import it : 

```bash
make tf-import-adls
``` 
##### CLI Step 6: Review Changes
Before applying changes, run the `make tf-plan` command to review the changes that will be made:
```bash
make tf-plan
```

##### CLI Step 7: Apply Changes
To apply the changes and create or update resources, run the following command:
```bash
make tf-apply
```

**Project SPN**
You can now retrieve the value of the Project  SPN Client ID and Secret from Entra ID / App Registrations in the Azure Portal.
The Project SPN has a `Contributor` role on the Resource Group, and `Set`, `Get`, `List` permissions on the Key Vault secrets. It should be used across resources to fuel Azure ML pipelines, as environment variables.

Azure portal: https://portal.azure.com/

### Destroy the infrastructure

#### GitHub Actions Destruction

##### Trigger Destruction Workflow
   1. Go to Actions → destroy_infra_terraform
   2. Click "Run workflow"
   3. Fill in required information:
      - Environment (dev/staging/prod)
      - Confirmation string (format: `DESTROY-INFRASTRUCTURE-[ENV]-[DATE]`)
      - Reason for destruction
      - Related ticket ID
   4. Click "Run workflow"

##### Secrets

To ensure the proper functioning of the destruction workflow, you need to set the following secrets in your GitHub repository:
 ```text
   # Azure Authentication
   AZURE_CLIENT_ID          # DevOps SPN Client ID
   AZURE_SUBSCRIPTION_ID    # Azure Subscription ID
   AZURE_TENANT_ID         # Azure Tenant ID
   ARM_SUBSCRIPTION_ID     # Azure Subscription ID
   
   # Terraform Variables
   TF_VAR_DEVOPS_SPN_OBJECT_ID           # Object ID of the DevOps SPN
   TF_VAR_TF_BACKEND_STORAGE_ACCOUNT_ID   # Storage Account ID for Terraform backend
   TF_VAR_USER_PASSWORD                   # Password for the Azure AD user

   SMTP_SERVER           # SMTP server address
   SMTP_PORT           # SMTP server port
   SMTP_USERNAME           # SMTP server username
   SMTP_PASSWORD           # SMTP server password
   EMAIL_NOTIFICATIONS           # Email addresses to notify for destruction
   ```

##### Safety Checks
   The workflow will automatically:
   - Verify confirmation string
   - Check business hours (Mon-Fri, 9 AM - 5 PM)
   - Verify user authorization
   - Send notification to stakeholders
   - Wait 10 minutes before proceeding

##### Monitor Destruction
   - View progress in GitHub Actions tab
   - Check destruction logs in artifacts
   - Await completion email notification

##### Manual Resource Cleanup
   You will have to manually purge from the Azure Portal:
   - Azure Key Vault
   - Azure ML Workspace
   Open their respective resource page, click on `Manage Deleted "resource"` and Purge.
   The ADLS account cannot be destroyed, and will be purged after a few days.

#### CLI Destruction

To destroy the infrastructure via CLI, run any of the following command:

```bash
make tf-destroy
make tf-destroy-aa
```
- `-aa` will destroy the infrastructure without asking for confirmation

You will have to manually purge from the Azure Portal:
  - Azure Key Vault
  - Azure ML Workspace
Open their respective resouce page, click on `Manage Deleted "resouce"` and Purge.
The ADLS account cannot be destoryed, and will be purged after a few days.

### Reinitialize the infrastructure

First, destroy the infrastructure as explained in [Destroy the infrastructure](#destroy-the-infrastructure).

// ... existing code ...

### Reinitialize the infrastructure

First, destroy the infrastructure as explained in [Destroy the infrastructure](#destroy-the-infrastructure).

#### GitHub Actions Reinitialization

##### Step 1: Resource Naming Changes

###### Recommended: New Project Name
If you wish to redeploy the infrastructure, update the following GitHub repository secrets:
```text
TF_VAR_RESOURCE_NAME_PREFIX      # New project name prefix
```

And update the following environment variables in the workflow files:
```yaml
env:
  TF_VAR_AUTH_APPLICATION_NAME_PREFIX: "new-app-name"
  AML_WORKSPACE_NAME: "new-workspace-name"
  AML_RESOURCE_GROUP: "new-resource-group"
  ABDS_NAME: "new-datastore-name"
  ABDS_ACCOUNT_NAME: "new-storage-account"
  ABDS_CONTAINER_NAME: "new-container-name"
```

###### Alternative: Same Project Name
If redeploying with the same project name:
1. Manually manage the following resources in Azure Portal:
   - Azure Key Vault: Either restore or purge and recreate
   - Azure ML Workspace: Either restore or purge and recreate
   - ADLS account: Will need to be restored (cannot be purged)

2. If restoring resources, they must be imported into Terraform state using the workflow:
   1. Go to Actions → import_resources_terraform
   2. Click "Run workflow"
   3. Select resources to import
   4. Click "Run workflow"

##### Step 2: Update User Credentials
Update the following GitHub secret:
```text
TF_VAR_USER_PASSWORD    # New user password
```

And update the following environment variables in the workflow files:
```yaml
env:
  TF_VAR_USER_PRINCIPAL_NAME_PREFIX: "new-user"
  TF_VAR_USER_DISPLAY_NAME: "New User"
```

##### Step 3: Redeploy Infrastructure
1. Go to Actions → deploy_infra_terraform
2. Click "Run workflow"
3. Select branch
4. Click "Run workflow"

##### Step 4: Update Environment Variables
After successful deployment, update the following GitHub secrets with values from Azure Portal:
```text
AZURE_CLIENT_ID        # New Project SPN Client ID
AZURE_CLIENT_SECRET    # New Project SPN Client Secret
ADLS_ACCOUNT_KEY       # New Storage Account Key
```

#### CLI Reinitialization

##### Step 1: Resouces naming changes

##### Recommended: new project name

If you wish to redeploy the infrastructure, it is recommended to change the name of the resources project name. The following environment variables are available to change the project name:
```dotenv
TF_VAR_resource_name_prefix=

TF_VAR_auth_application_name_prefix=

AML_WORKSPACE_NAME=
AML_RESOURCE_GROUP=

ABDS_NAME=

ABDS_ACCOUNT_NAME=
ABDS_CONTAINER_NAME=
```

##### Alternative: same project name

If you want to redeploy the infrastructure with the same project name, you can skip the naming changes.

You need to manage the following resources manually

**Azure Key Vault**
You can either restore the existing Key Vault from the Azure Portal, or purge it from the soft-deleted resource page and create a new one. If you restore it, you will have to import it using the following command:

```bash
# Key Vault
terraform import azurerm_key_vault.example /subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.KeyVault/vaults/{vault_name}
```

**Azure ML Workspace**
You can either restore the existing Azure ML Workspace from the Azure Portal, or purge it from the soft-deleted resource page and create a new one. If you restore it, you will have to import it using the following command:

```bash
# Azure ML Workspace
terraform import azurerm_machine_learning_workspace.example /subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.MachineLearningServices/workspaces/{workspace_name}
```

**Azure Data Lake Storage (ADLS) account**
The ADLS account cannot be destoryed, and will be purged after a few days. You can restore it from the Azure Portal. If you restore it, you will have to import it using the following command:

```bash
# Storage Account
terraform import azurerm_storage_account.example /subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.Storage/storageAccounts/{storage_account_name}
```

#### User name and password
For any deployment, it is recommended to change the user name and password. The following environment variables are available to change the user name and password:
```dotenv
TF_VAR_user_principal_name_prefix=
TF_VAR_user_display_name=
TF_VAR_user_password=
```

##### Step 2: Redeploy the infrastructure
To reinitialize the infrastructure, run any of the following command:

- For one-command auto-approve full redeployment:
```bash
make tf-apply-aa
```

- For a 2-step plan and apply:
```bash
make tf-plan
make tf-apply
```

##### Step 3: Update environment variables
Then you can update the environment variables from Azure Portal:
```dotenv
# For the Project SPN
ARM_CLIENT_ID=

# For the Project SPN
ARM_CLIENT_SECRET=

ADLS_ACCOUNT_KEY=
```

### Conclusion on infrastructure deployment
This documentation provides the necessary steps to deploy Azure ML and associated services using Terraform. Ensure you have set all required environment variables, authenticate to Azure correctly, and follow the outlined steps for a successful deployment from Github Actions or CLI.


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

### Priority level 0 - WIP
Bug fixes, critical improvements, current sprint tasks.
- Testing full deployments and destruction of the infrastructure for both dev and prd environments

### Priority level 1 - HOT
Top priority new features, next sprint tasks.
-  Training
  - Add a command to train a model in the Azure ML workspace.
  - Add a command to register the model in the Azure ML workspace.
  - Add a command to deploy the model as an always-on endpoint in the Azure ML workspace.
  - Add a command to deploy the model in a batch inference pipeline in the Azure ML workspace.

### Priority level 2 - WARM
December 2024 tasks.
- Fix iac/script/purge_resouces.sh to purge the resources without having to go to the Azure Portal.
- Fix key_vault.tf to include the secrets from the Key Vault.
- Inference
  - Add a command to run a batch inference pipeline in the Azure ML workspace.
  - Add a command to run a batch inference pipeline in the Azure ML workspace with a model registered in the workspace.

- Monitoring
  - Add a command to set the monitoring configuration in the Azure ML workspace.
  - Add a command to retrieve the monitoring logs of the Azure ML workspace.
  - 
### Priority level 3 - COLD
January 2025 tasks.

- Documentation
  - Add a section in the README.md file to explain how to deploy the package in a CICD pipeline.

- Tests
  - Repair tests in `tests/services/test_ml_client.py` and `tests/services/data/test_data.py`. 
  Most issues seems to come from a bad use of mocking.

- Terraform
  - Add the `env/prd/` folder and the `make tf-init` command to initialize the production workspace.
  - Some values are hardcoded in the Terraform code. They should be set as variables in the `variables.tf` file 
  and declared as environment variables `TF_VAR_xxx` in the template `.env` file in the `README.md` file.