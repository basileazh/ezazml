# All settings are stored in the Settings class. Values are read from environment variables or a .env file.
# Created: 2024-07
# Created by: Basile El Azhari
# Maintained by: Basile El Azhari
# Contact: basile.elazhari@ekimetrics.com, https://www.linkedin.com/in/basile-el-azhari/

from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

from ezazml.core.settings import get_settings


settings = get_settings()


def get_ml_client() -> MLClient:
    """
    Get an Azure ML client.
    """
    return MLClient(
        DefaultAzureCredential(),
        settings.aml.AZURE_SUBSCRIPTION_ID,
        settings.aml.AML_RESOURCE_GROUP,
        settings.aml.AML_WORKSPACE_NAME,
    )
