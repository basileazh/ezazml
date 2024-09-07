# All settings are stored in the Settings class. Values are read from environment variables or a .env file.
# Created: 2024-07
# Created by: Basile El Azhari
# Maintained by: Basile El Azhari
# Contact: basile.elazhari@ekimetrics.com, https://www.linkedin.com/in/basile-el-azhari/

import os
from pydantic_settings import (
    BaseSettings,
)


# Path to root app/ directory
DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class AzureMLSettings(BaseSettings):
    """
    Azure ML settings.
    Values are read from environment variables.
    """

    AML_WORKSPACE_NAME: str = ""
    AML_SUBSCRIPTION_ID: str = ""
    AML_RESOURCE_GROUP: str = ""
    AML_ACTIVATE_MLTABLES: bool = True


class ADLSDatastoreSettings(BaseSettings):
    """
    ADLS settings.
    To activate ADLS, set ACTIVATE_ADLS to True and provide the ADLS_ACCOUNT_KEY.
    When activated, the data paths provided via CLI will point to an Azure Blob Datastore.
    If not activated, the data paths provided via CLI will point to a local directory.
    ABDS variables are used to create or access an Azure Blob Datastore in Azure ML.
    Values are read from environment variables.
    """

    ADLS_ACTIVATE: bool = False
    ADLS_ACCOUNT_KEY: str | None = None

    ABDS_NAME: str | None = "AzureMLAzureBlobDatastore"
    ABDS_DESCRIPTION: str | None = (
        "Datastore pointing to a blob container using https protocol."
    )
    ABDS_ACCOUNT_NAME: str | None = "mytestblobstoreaccount"
    ABDS_CONTAINER_NAME: str | None = "data-container"
    ABDS_PROTOCOL: str | None = "https"


class DatabricksSettings(BaseSettings):
    """
    Databricks settings.
    Values are read from environment variables.
    """

    DATABRICKS_ACTIVATE: bool = False
    DATABRICKS_HOST: str = ""  # Databricks workspace hostname (e.g. adb-<some-number>.<two digits>.azuredatabricks.net)
    DATABRICKS_PAT: str = ""  # Databricks personal access token
    DATABRICKS_DBFS_PREFIX: str = "dbfs://"


class LoggingSettings(BaseSettings):
    """
    Logging settings.
    Values are read from environment variables.
    """

    LOG_FILE_PATH_TEMPLATE: str = "logs/[DATETIME_PLACEHOLDER]_app.log"
    LOG_FORMAT: str = (
        "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s"
    )
    LOG_FILE_PATH: str = os.path.join(DIR, LOG_FILE_PATH_TEMPLATE)
    LOG_DATETIME_FORMAT: str = "%Y-%m-%d_%H"


class Settings:
    """
    All settings for the application.
    """

    # App settings
    log: LoggingSettings = LoggingSettings()

    # Azure ML settings
    aml: AzureMLSettings = AzureMLSettings()

    # Azure ML ADLS Datastore settings
    aml_adls: ADLSDatastoreSettings = ADLSDatastoreSettings()

    # Databricks settings
    databricks: DatabricksSettings = DatabricksSettings()


def get_settings():
    """
    Get the settings for the application.
    :return: Settings object with all settings from env vars.
    :rtype: Settings
    """
    return Settings()
