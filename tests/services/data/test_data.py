# import pytest
# from unittest.mock import Mock, patch
# import pandas as pd
#
# from ezazml.services.data.data import AmlDataService, DataSourceEnum, AMLFSOverwriteModeEnum, AzureMLTablesAssetTypesEnum
#
#
# @pytest.fixture
# def aml_data_service():
#     with patch('from ezazml.core.settings.get_settings'), patch('from ezazml.core.settings.get_ml_client'):
#         service = AmlDataService()
#         service.ACTIVATE_ADLS = True
#         service.ACTIVATE_DATABRICKS = True
#         service.SUBSCRIPTION_ID = "sub123"
#         service.RESOURCE_GROUP = "rg123"
#         service.WORKSPACE_NAME = "ws123"
#         service.ABDS_NAME = "abds123"
#         return service
#
#
# def test_create_or_update_adls_gen2_datastore(aml_data_service):
#     with patch('your_module.AzureBlobDatastore') as mock_datastore, \
#             patch('your_module.get_ml_client') as mock_get_ml_client:
#         mock_ml_client = Mock()
#         mock_get_ml_client.return_value = mock_ml_client
#
#         aml_data_service.create_or_update_adls_gen2_datastore()
#
#         mock_datastore.assert_called_once()
#         mock_ml_client.create_or_update.assert_called_once()
#
#
# def test_create_mltable(aml_data_service):
#     with patch('your_module.mltable') as mock_mltable, \
#             patch.object(aml_data_service, 'create_dataset') as mock_create_dataset:
#         mock_tbl = Mock()
#         mock_mltable.from_delimited_files.return_value = mock_tbl
#
#         aml_data_service.create_mltable(["data.csv"], "mltable_path")
#
#         mock_mltable.from_delimited_files.assert_called_once()
#         mock_tbl.save.assert_called_once_with("mltable_path")
#         mock_create_dataset.assert_called_once()
#
#
# def test_create_dataset(aml_data_service):
#     with patch.object(aml_data_service, 'ml_client') as mock_ml_client:
#         aml_data_service.create_dataset("data.csv")
#
#         mock_ml_client.data.create_or_update.assert_called_once()
#
#
# def test_get_dataframe_from_mltable(aml_data_service):
#     with patch.object(aml_data_service, 'ml_client') as mock_ml_client, \
#             patch('your_module.mltable') as mock_mltable:
#         mock_data_asset = Mock()
#         mock_ml_client.data.get.return_value = mock_data_asset
#         mock_tbl = Mock()
#         mock_mltable.load.return_value = mock_tbl
#         mock_df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
#         mock_tbl.to_pandas_dataframe.return_value = mock_df
#
#         result = aml_data_service.get_dataframe(mltable_name="test_mltable", mltable_version="1")
#
#         pd.testing.assert_frame_equal(result, mock_df)
#         mock_ml_client.data.get.assert_called_once_with(name="test_mltable", version="1")
#         mock_mltable.load.assert_called_once()
#
#
# def test_get_dataframe_from_file(aml_data_service):
#     with patch('your_module.pd.read_csv') as mock_read_csv:
#         mock_df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
#         mock_read_csv.return_value = mock_df
#
#         result = aml_data_service.get_dataframe(path="data.csv")
#
#         pd.testing.assert_frame_equal(result, mock_df)
#         mock_read_csv.assert_called_once()
#
#
# def test_get_uri_datastore(aml_data_service):
#     result = aml_data_service._get_uri_datastore("data.csv")
#     expected = "azureml://subscriptions/sub123/resourcegroups/rg123/workspaces/ws123/datastores/abds123/paths/data.csv"
#     assert result == expected
#
#
# def test_get_uri_databricks(aml_data_service):
#     aml_data_service.DBFS_PREFIX = "dbfs://"
#     result = aml_data_service._get_uri_databricks("data.csv")
#     assert result == "dbfs://data.csv"
#
#
# def test_upload_file_to_datastore(aml_data_service):
#     with patch('your_module.AzureMachineLearningFileSystem') as mock_fs:
#         mock_fs_instance = Mock()
#         mock_fs.return_value = mock_fs_instance
#
#         aml_data_service.upload_file_to_datastore("local_path.csv", "remote_path.csv")
#
#         mock_fs.assert_called_once()
#         mock_fs_instance.upload.assert_called_once_with(
#             lpath="local_path.csv",
#             rpath="remote_path.csv",
#             recursive=False,
#             overwrite="MERGE_WITH_OVERWRITE"
#         )
#
#
# def test_get_file_extension():
#     from your_module import get_file_extension
#     assert get_file_extension("data.csv") == "csv"
#     assert get_file_extension("path/to/data.parquet") == "parquet"
#
#
# def test_get_mlt_asset_type():
#     from your_module import get_mlt_asset_type
#     assert get_mlt_asset_type("data.csv") == AzureMLTablesAssetTypesEnum.FILE.value
#     assert get_mlt_asset_type("data_folder") == AzureMLTablesAssetTypesEnum.FOLDER.value
#     assert get_mlt_asset_type("data*.csv") == AzureMLTablesAssetTypesEnum.PATTERN.value
#
#
# def test_format_input_mlt():
#     from your_module import format_input_mlt
#     result = format_input_mlt(["data.csv", "folder", "data*.parquet"])
#     expected = [
#         {"file": "data.csv"},
#         {"folder": "folder"},
#         {"pattern": "data*.parquet"}
#     ]
#     assert result == expected
