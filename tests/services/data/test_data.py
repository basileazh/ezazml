import pytest
from unittest.mock import Mock, patch

from azure.ai.ml.entities import AzureBlobDatastore
from mltable import mltable
from ezazml.services.data.data import AmlDataService
from ezazml.core.settings import Settings
from ezazml.services.data.models import DataSourceEnum, MltFromTypeEnum


@pytest.fixture
def mock_settings():
    settings = Mock(spec=Settings)
    settings.aml.AML_WORKSPACE_NAME = "test_workspace"
    settings.aml.AZURE_SUBSCRIPTION_ID = "test_subscription"
    settings.aml.AML_RESOURCE_GROUP = "test_resource_group"
    settings.aml_adls.ADLS_ACTIVATE = True
    settings.aml_adls.ADLS_ACCOUNT_KEY = "test_account_key"
    settings.aml_adls.ABDS_NAME = "test_abds_name"
    settings.aml_adls.ABDS_DESCRIPTION = "test_abds_description"
    settings.aml_adls.ABDS_ACCOUNT_NAME = "test_abds_account_name"
    settings.aml_adls.ABDS_CONTAINER_NAME = "test_abds_container_name"
    settings.aml_adls.ABDS_PROTOCOL = "test_abds_protocol"
    settings.databricks.DATABRICKS_ACTIVATE = True
    settings.databricks.DATABRICKS_HOST = "test_databricks_host"
    settings.databricks.DATABRICKS_PAT = "test_databricks_pat"
    settings.databricks.DATABRICKS_DBFS_PREFIX = "test_databricks_dbfs_prefix"
    return settings


@pytest.fixture
def mock_ml_client():
    ml_client = Mock()
    ml_client.data = Mock()
    return ml_client


@pytest.fixture
def aml_data_service(mock_settings, mock_ml_client):
    with patch("ezazml.core.settings.get_settings", return_value=mock_settings):
        with patch(
            "ezazml.services.ml_client.get_ml_client", return_value=mock_ml_client
        ):
            yield AmlDataService()


def test_create_or_update_adls_gen2_datastore(aml_data_service, mock_ml_client):
    store = aml_data_service.create_or_update_adls_gen2_datastore()
    assert isinstance(store, AzureBlobDatastore)


def test_create_mltable(aml_data_service, mock_ml_client):
    mock_mltable = Mock(spec=mltable)
    mock_mltable.save = Mock()
    with patch("mltable.mltable.from_delimited_files", return_value=mock_mltable):
        aml_data_service.create_mltable(["test_path"], "test_mltable_save_path")


# TODO: Fix this test
# def test_create_dataset(aml_data_service, mock_ml_client):
#     with patch("azure.ai.ml.entities._assets._artifacts.data.Data", autospec=True) as mock_dataset_cls:
#         mock_dataset = mock_dataset_cls.return_value
#         aml_data_service.create_dataset(
#             "test_path",
#             asset_type=AssetTypes.URI_FILE,
#             data_description="test_data_description",
#             data_name="test_data_name"
#         )

# TODO: Fix this test
# def test_get_dataframe(aml_data_service, mock_ml_client):
#     with patch("mltable.load", return_value=Mock(spec=mltable)):
#         df = aml_data_service.get_dataframe(mltable_name="test_mltable_name", mltable_version="test_mltable_version")
#         assert isinstance(df, DataFrame)


def test_get_uri(aml_data_service):
    uri = aml_data_service.get_uri(
        "test_path.test", data_source=DataSourceEnum.datastore
    )
    assert isinstance(uri, str)


# TODO: Fix this test
# def test_upload_file_to_datastore(aml_data_service):
#     with patch("azureml.fsspec.spec.AzureMachineLearningFileSystem") as mock_fs:
#         uri = aml_data_service.upload_file_to_datastore("test_source_path.test", "test_dest_path.test")
#         assert uri == "test_dest_path.test"


def test_create_or_update_adls_gen2_datastore_no_account_key(aml_data_service):
    aml_data_service.ADLS_ACCOUNT_KEY = None
    with pytest.raises(ValueError):
        aml_data_service.create_or_update_adls_gen2_datastore()


def test_create_mltable_different_extensions(aml_data_service, mock_ml_client):
    with patch("mltable.mltable.from_delimited_files", return_value=Mock(spec=mltable)):
        aml_data_service.create_mltable(
            ["test_path"],
            "test_mltable_save_path",
            inputs_extension=MltFromTypeEnum.parquet,
        )


# TODO: Fix this test
# def test_create_dataset_different_asset_type(aml_data_service, mock_ml_client):
#     with pytest.raises(ValueError):
#         aml_data_service.create_dataset("test_path", asset_type=AssetTypes.URI_FILE)


def test_get_dataframe_no_mltable_name_or_path(aml_data_service):
    with pytest.raises(ValueError):
        aml_data_service.get_dataframe()


def test_get_dataframe_both_mltable_name_and_path(aml_data_service):
    with pytest.raises(ValueError):
        aml_data_service.get_dataframe(
            mltable_name="test_mltable_name", path="test_path"
        )


def test_get_dataframe_mltable_name_without_version(aml_data_service):
    with pytest.raises(ValueError):
        aml_data_service.get_dataframe(mltable_name="test_mltable_name")


def test_get_uri_unsupported_data_source(aml_data_service):
    with pytest.raises(ValueError):
        aml_data_service.get_uri("test_path", data_source="unsupported_data_source")


# TODO: Fix this test
# def test_upload_file_to_datastore_different_asset_type(aml_data_service):
#     with patch("azureml.fsspec.spec.AzureMachineLearningFileSystem") as mock_fs:
#         uri = aml_data_service.upload_file_to_datastore("test_source_path", "test_dest_path", asset_type=AssetTypes.URI_FOLDER)
#         assert uri == "test_dest_path"
