# Created: 2024-07
# Created by: Basile El Azhari
# Maintained by: Basile El Azhari
# Contact: basile.elazhari@ekimetrics.com, https://www.linkedin.com/in/basile-el-azhari/
from typing import Any

import pandas as pd
from mltable import mltable, MLTableHeaders, MLTableFileEncoding
from azure.ai.ml.entities import AzureBlobDatastore
from azure.ai.ml.entities import AccountKeyConfiguration
from azure.ai.ml import MLClient
from azure.ai.ml.entities import Data
from azure.ai.ml.constants import AssetTypes
from azureml.fsspec import AzureMachineLearningFileSystem

from ezazml.core.log import logger
from ezazml.core.settings import Settings, get_settings
from ezazml.services.ml_client import get_ml_client
from .models import (
    AzureMLTablesAssetTypesEnum,
    DataSourceEnum,
    AMLFSOverwriteModeEnum,
    MltFromTypeEnum,
    PANDAS_READ_MAPPING,
)


class AmlDataService:
    """
    Azure Machine Learning data service.
    All data-related operations are done here.
    All settings used are declared in the init method.

    Example usage:
    data_service = AmlDataService()
    """

    DATASTORE_URI_FORMAT = "azureml://subscriptions/{subscription}/resourcegroups/{resource_group}/workspaces/{workspace}/datastores/{datastore_name}/paths/{path_on_datastore}"

    def __init__(self):
        self.settings: Settings = get_settings()
        self.ml_client: MLClient = get_ml_client()

        # Azure ML settings
        self.WORKSPACE_NAME: str = self.settings.aml.AML_WORKSPACE_NAME
        self.SUBSCRIPTION_ID: str = self.settings.aml.AZURE_SUBSCRIPTION_ID
        self.RESOURCE_GROUP: str = self.settings.aml.AML_RESOURCE_GROUP

        # ADLS Gen2 & AML Datastore settings
        self.ACTIVATE_ADLS: bool = self.settings.aml_adls.ADLS_ACTIVATE
        self.ADLS_ACCOUNT_KEY: str = self.settings.aml_adls.ADLS_ACCOUNT_KEY
        self.ABDS_NAME: str = self.settings.aml_adls.ABDS_NAME
        self.ABDS_DESCRIPTION: str = self.settings.aml_adls.ABDS_DESCRIPTION
        self.ABDS_ACCOUNT_NAME: str = self.settings.aml_adls.ABDS_ACCOUNT_NAME
        self.ABDS_CONTAINER_NAME: str = self.settings.aml_adls.ABDS_CONTAINER_NAME
        self.ABDS_PROTOCOL: str = self.settings.aml_adls.ABDS_PROTOCOL

        # Databricks settings
        self.ACTIVATE_DATABRICKS: bool = self.settings.databricks.DATABRICKS_ACTIVATE
        self.DATABRICKS_HOST: str = self.settings.databricks.DATABRICKS_HOST
        self.DATABRICKS_PAT: str = self.settings.databricks.DATABRICKS_PAT
        self.DBFS_PREFIX: str = self.settings.databricks.DATABRICKS_DBFS_PREFIX

    def create_or_update_adls_gen2_datastore(self) -> AzureBlobDatastore:
        """
        Create an ADLS Gen2 datastore in Azure ML that references an ADLS Gen2 account.
        ADLS_ACCOUNT_KEY is needed to create the datastore.
        :return: The ADLS Gen2 datastore.
        :rtype: AzureBlobDatastore

        Example usage:
        # Check that ACTIVATE_ADLS env var is True and ADLS_ACCOUNT_KEY env var is provided
        data_service = AmlDataService()  # Initialize the data service
        store = data_service.create_or_update_adls_gen2_datastore()
        """
        if self.ACTIVATE_ADLS & (self.ADLS_ACCOUNT_KEY is not None):
            store = AzureBlobDatastore(
                name=self.ABDS_NAME,
                description=self.ABDS_DESCRIPTION,
                account_name=self.ABDS_ACCOUNT_NAME,
                container_name=self.ABDS_CONTAINER_NAME,
                protocol=self.ABDS_PROTOCOL,
                credentials=AccountKeyConfiguration(account_key=self.ADLS_ACCOUNT_KEY),
            )
            ml_client = get_ml_client()
            ml_client.create_or_update(store)
        else:
            raise ValueError(
                "To create an ADLS Gen2 datastore, ACTIVATE_ADLS must be True and ADLS_ACCOUNT_KEY must be provided."
            )

        return store

    def create_mltable(
        self,
        input_paths: list[str],
        mltable_save_path: str,
        inputs_extension: str = MltFromTypeEnum.csv,
        headers: MLTableHeaders = MLTableHeaders.all_files_same_headers,
        data_description: str = "",
        data_version: str | None = None,
        infer_column_types: bool = True,
        include_path_column: bool = False,
        keep_columns: list[str] = [],
        drop_columns: list[str] = [],
        filter_lines: str | None = None,
    ) -> None:
        """
        Create a mltable from a Pandas DataFrame and save it in the datastore.
        The datastore must be created before creating the mltable.
        :param input_paths: Paths to the data in the datastore. Can be a file, folder or pattern, or list of multiple/mix them.
        Must be in a list if files types are csv, parquet or json, and must only be a string if the file type is delta_lake.
        :example: file ["wasbs://data@azuremlexampledata.blob.core.windows.net/titanic.csv"]
        :example: pattern ["wasbs://nyctlc@azureopendatastorage.blob.core.windows.net/green/puYear=2015/puMonth=*/*.parquet"]
        :example: folder ["wasbs://data@<account_name>.blob.core.windows.net/data"]
        :example: "wasbs://data@<account_name>.blob.core.windows.net/data_delta_table"
        :type input_paths: list[str]
        :param mltable_save_path: The path to save the mltable in the datastore. Example: "./titanic_mlt"
        :type mltable_save_path: str
        :param inputs_extension: The extensions of the input files. Default is "csv". Other options are "parquet" and "json".
        :type inputs_extension: str
        :param headers: The headers of the mltable. Default is "all_files_same_headers". Other options are "no_headers" and "from_first_file", "all_files_different_headers"
        :type headers: MLTableHeaders
        :param data_description: The description of the mltable.
        :type data_description: str
        :param data_version: The version of the mltable. If not provided, the last version +1 is used.
        :type data_version: str | None
        :param infer_column_types: Whether to infer the column types. Default is True.
        :type infer_column_types: bool
        :param include_path_column: Whether to include the path column. Default is False.
        :type include_path_column: bool
        :param keep_columns: The features to keep in the mltable. Default is [] (all features).
        :type keep_columns: list of str
        :param drop_columns: The features to drop in the mltable. Default is [] (no features).
        :type drop_columns: list of str
        :param filter_lines: The filter to apply to the mltable for lines, in pyspark.sql format.
        :example: "col('Age') > 0"
        :example:filtered_mltable = mltable.filter('feature_1 == "5" and target > "0.5)"')
        :example:filtered_mltable = mltable.filter('col("FBI Code") == "11"')
        :type filter_lines: str | None
        :raises ValueError: If the file format is not supported.

        Example usage:
        data_service = AmlDataService()
        data = pd.read_csv("data.csv")
        data_service.create_mltable(["data.csv"], "data_mltable")
        """
        # Create the mltable
        if inputs_extension == MltFromTypeEnum.csv:  # Case csv
            input_paths_mlt = format_input_mlt(input_paths)
            logger.info(f"input_paths_mlt: {input_paths_mlt}")
            tbl = mltable.from_delimited_files(
                input_paths_mlt,
                header=headers,
                infer_column_types=infer_column_types,
                include_path_column=include_path_column,
                encoding=MLTableFileEncoding.utf8,
            )
        elif inputs_extension == MltFromTypeEnum.parquet:  # Case parquet
            input_paths_mlt = format_input_mlt(input_paths)
            tbl = mltable.from_parquet_files(
                input_paths_mlt, include_path_column=include_path_column
            )
        elif inputs_extension == MltFromTypeEnum.json:  # Case json
            input_paths_mlt = format_input_mlt(input_paths)
            tbl = mltable.from_json_lines_files(
                input_paths_mlt,
                include_path_column=include_path_column,
                encoding=MLTableFileEncoding.utf8,
            )
        elif inputs_extension == MltFromTypeEnum.delta_lake:  # Case delta_lake
            tbl = mltable.from_delta_lake(
                input_paths, include_path_column=include_path_column
            )
        else:  # Case non tabular data, like images or text files
            input_paths_mlt = format_input_mlt(input_paths)
            tbl = mltable.from_paths(input_paths_mlt)

        # Filtering lines and columns with pyspark.sql like syntax
        if filter_lines:
            tbl = tbl.filter(filter_lines)

        # Filtering columns
        if keep_columns:
            tbl = tbl.keep_columns(keep_columns)
        if drop_columns:
            tbl = tbl.drop_columns(drop_columns)

        logger.info("mltable show: print(tbl.show())")

        # Save the data loading steps in an MLTable file
        tbl.save(mltable_save_path)

        # Create a data asset in Azure ML
        mltable_name = mltable_save_path.split("/")[-1]
        self.create_dataset(
            path=mltable_save_path,
            asset_type=AssetTypes.MLTABLE,
            data_name=mltable_name,
            data_description=data_description,
            data_version=data_version,
        )

    def create_dataset(
        self,
        path: str,
        asset_type: str = AssetTypes.URI_FILE,
        data_description: str | None = None,
        data_name: str | None = None,
        data_version: str | None = None,
    ) -> None:
        """
        Create a dataset in Azure ML that references a file in a datastore.
        The datastore must be created before creating the dataset.
        :param path: The path to the file in the datastore.
        :type path: str
        :param asset_type: The type of asset. Default is "uri_file". Other options are "uri_folder" and "mltable".
        :type asset_type: str
        :param data_description: The description of the dataset.
        :type data_description: str
        :param data_name: The name of the dataset.
        :type data_name: str
        :param data_version: The version of the dataset. If not provided, the last version +1 is used.
        :type data_version: str | None

        Example usage:
        data_service = AmlDataService()
        data_service.create_dataset("data.csv")
        """
        data = Data(
            path=path,
            type=asset_type,
            description=data_description,
            name=data_name,
            version=data_version,
        )
        self.ml_client.data.create_or_update(data)

    def get_dataframe(
        self,
        mltable_name: str | None = None,
        mltable_version: str | None = None,
        path: str | None = None,
        data_source: str | None = DataSourceEnum.local,
        data_features: list[str] | None = None,
        **kwargs: dict[str, Any],
    ) -> pd.DataFrame:
        """
        Get a Pandas DataFrame from a mltable, file or folder in the datastore. The file(s) format must be CSV, Parquet or JSON (file only).
        For a more specific file format, please use the get_file_uri_from_datastore method.
        One of mltable_name or path must be provided.
        :param mltable_name: The path to the mltable in the datastore. Default is None.
        :type mltable_name: str | None
        :param mltable_version: The version of the mltable. Default is None.
        :type mltable_version: str | None
        :param path: The path to the file or folder in the datastore.
        :type path: str
        :param data_source: The source of the data. Default is "datastore". Other options are "databricks".
        :type data_source: str
        :param data_features: The features to keep in the DataFrame. Default is None (all features).
        :type data_features: list of str | None
        :param kwargs: Additional arguments to pass to the Pandas read_csv, read_parquet or read_json method in case the resource is given as a path is not a mltable.
        :type kwargs: dict of str, any
        :return: The Pandas DataFrame.
        :rtype: pd.DataFrame

        Example usage:
        data_service = AmlDataService()
        data = data_service.get_dataframe("data.csv")
        """
        # Check the parameters
        if (path is None) & (mltable_name is None):
            raise ValueError("Either path or mltable_name must be provided.")
        if (path is not None) & (mltable_name is not None):
            raise ValueError("Only one of path or mltable_name must be provided.")
        if (mltable_name is not None) & (mltable_version is None):
            raise ValueError(
                "If mltable_name is provided, mltable_version must be provided."
            )

        # Get the storage options
        storage_options: dict[str, str] | None = None
        if self.ACTIVATE_DATABRICKS & (data_source == DataSourceEnum.databricks):
            storage_options = {
                "host": self.DATABRICKS_HOST,
                "token": self.DATABRICKS_PAT,
            }

        # Get the dataframe
        df: pd.DataFrame | None = None

        # Case we load a dataset recorded as a mltable
        if mltable_name is not None:
            data_asset = self.ml_client.data.get(
                name=mltable_name, version=mltable_version
            )
            tbl = mltable.load(f"azureml:/{data_asset.id}")
            df = tbl.to_pandas_dataframe()

        # Case the dataset in not a mltable
        elif path is not None:
            file_extension = get_file_extension(path)
            mlt_asset_type = get_mlt_asset_type(path)

            # Subcase folder or pattern
            if mlt_asset_type in (
                AzureMLTablesAssetTypesEnum.PATTERN.value,
                AzureMLTablesAssetTypesEnum.FOLDER.value,
            ):
                # create the filesystem
                fs = AzureMachineLearningFileSystem(self._get_uri_datastore())
                # append parquet files in folder to a list
                df_list = []
                # get all files in the folder from their extension
                for path in fs.glob(f"{path}"):
                    with fs.open(path) as f:
                        df_list.append(
                            PANDAS_READ_MAPPING[file_extension](
                                f, storage_options=storage_options, **kwargs
                            )
                        )
                # concatenate all the dataframes
                df = pd.concat(df_list)

            # Subcase file
            else:
                df = PANDAS_READ_MAPPING[file_extension](
                    path, storage_options=storage_options, **kwargs
                )
        else:
            raise ValueError("No path or mltable_name provided.")

        # Filtering columns
        if data_features is not None:
            df = df[data_features]

        return df

    def get_uri(self, path: str, data_source: str = DataSourceEnum.datastore) -> str:
        """
        Get the URI of a file in the datastore or Databricks. The URI can be used with Pandas or any other library that supports it.
        :param path: The path to the file.
        :type path: str
        :param data_source: The source of the data. Default is "datastore". Other options are "databricks" and "local".
        :type data_source: str
        :return: The URI of the file.
        :rtype: str
        :raises ValueError: If the data source is not supported.

        Example usage:
        file_path = AmlDataService().get_uri("data.csv")
        data = pd.read_csv(file_path)
        """
        ## Case data on ADLS
        if (data_source == DataSourceEnum.datastore) & self.ACTIVATE_ADLS:
            return self._get_uri_datastore(path)
        ## Case data on Databricks
        elif (data_source == DataSourceEnum.databricks) & self.ACTIVATE_DATABRICKS:
            return self._get_uri_databricks(path)
        ## Case data local
        elif data_source == DataSourceEnum.local:
            return path
        else:
            raise ValueError(
                f"Data source : {data_source} not supported. Only 'datastore', 'databricks' and 'local' are supported."
            )

    def upload_file_to_datastore(
        self,
        source_path: str,
        dest_path: str,
        asset_type: str = AssetTypes.URI_FILE,
        overwrite: str = AMLFSOverwriteModeEnum.overwrite,
    ) -> str:
        """
        Upload a file to the datastore.
        :param source_path: The local path to the file to upload.
        :type source_path: str
        :param dest_path:  The path to the file in the datastore.
        :type dest_path: str
        :param asset_type: The type of asset to upload. Default is "uri_file". Other options are "uri_folder" and "mltable".
        :type asset_type: AssetTypes
        :param overwrite: The overwrite mode. Default is "MERGE_WITH_OVERWRITE". Other options are "APPEND" and "FAIL_ON_FILE_CONFLICT".
        :type overwrite: str
        :return: The URI of the file in the datastore.
        :rtype: str

        Example usage:
        data_service = AmlDataService()
        uri = data_service.upload_file_to_datastore("data.csv", "data.csv")
        """
        uri = self._get_uri_datastore()
        fs = AzureMachineLearningFileSystem(uri)
        recursive = False if asset_type == AssetTypes.URI_FILE else True
        fs.upload(
            lpath=source_path,
            rpath=dest_path,
            recursive=recursive,
            **{"overwrite": overwrite},
        )

        return dest_path

    # def download_file_from_datastore(
    #         self,
    #         source_path: str,
    #         dest_path: str,
    #         asset_type: str = AssetTypes.URI_FILE,
    #         overwrite: str = AMLFSOverwriteModeEnum.overwrite,
    # ) -> str:
    #     """
    #     Download a file from the datastore to the local machine.
    #     :param dest_path: The local path to save the file.
    #     :type dest_path: str
    #     :param source_path: The path to the file in the datastore.
    #     :type source_path: str
    #     :param asset_type: The type of asset to download. Default is "uri_file". Other options are "uri_folder" and "mltable".
    #     :type asset_type: AssetTypes
    #     :param overwrite: The overwrite mode. Default is "MERGE_WITH_OVERWRITE". Other options are "APPEND" and "FAIL_ON_FILE_CONFLICT".
    #     :type overwrite: str
    #     :return: The local path of the file.
    #     :rtype: str
    #
    #     Example usage:
    #     data_service = AmlDataService()
    #     data_service.download_file_from_datastore("data.csv", "data.csv")
    #     """
    #     uri = self._get_uri_datastore()
    #     fs = AzureMachineLearningFileSystem(uri)
    #     recursive = False if asset_type == AssetTypes.URI_FILE else True
    #     fs.download(
    #         lpath=source_path,
    #         rpath=dest_path,
    #         recursive=recursive,
    #         **{"overwrite": overwrite},
    #     )
    #
    #     return dest_path

    def _get_uri_datastore(self, path: str = "") -> str:
        """
        Get the URI of a file in the datastore. The URI can be used with Pandas or any other library that supports it.
        :param path: The subscription ID.
        :type path: str
        :return: The URI of the datastore.
        :rtype: str

        Example usage:
        data_service = AmlDataService()
        file_path = data_service.get_file_from_datastore_uri("data.csv")
        data = pd.read_csv(file_path)
        """
        return self.DATASTORE_URI_FORMAT.format(
            subscription=self.SUBSCRIPTION_ID,
            resource_group=self.RESOURCE_GROUP,
            workspace=self.WORKSPACE_NAME,
            datastore_name=self.ABDS_NAME,
            path_on_datastore=path,
        )

    def _get_uri_databricks(self, path: str) -> str:
        """
        Get the URI of a file in Databricks. The URI can be used with Pandas or any other library that supports it.
        :param path: The path to the file in Databricks.
        :type path: str
        :return: The URI of the file in Databricks.
        :rtype: str

        Example usage:
        file_path = AmlDataService.get_file_from_databricks_uri("data.csv")
        data = pd.read_csv(file_path)
        """
        return f"{self.DBFS_PREFIX}{path}"


def get_file_extension(file_path: str) -> str:
    """
    Get the extension of a file.
    :param file_path: The path to the file.
    :type file_path: str
    :return: The extension of the file.
    :rtype: str

    Example usage:
    extension = get_file_extension("data.csv")
    """
    return file_path.split(".")[-1]


def get_mlt_asset_type(file_path: str) -> str:
    """
    Get the Azure mltables asset type of file, folder or pattern.
    :param file_path: The path to the file.
    :type file_path: str
    :return: The asset type of the file.
    :rtype: AzureMLTablesAssetTypesModel

    Example usage:
    asset_type = get_asset_type("data.csv")
    """
    if len(file_path.split(".")) == 1:
        return AzureMLTablesAssetTypesEnum.FOLDER.value

    if "*" in file_path:
        return AzureMLTablesAssetTypesEnum.PATTERN.value

    return AzureMLTablesAssetTypesEnum.FILE.value


def format_input_mlt(input_paths: list[str]) -> list[dict[str, str]]:
    """
    Format the input paths for mltable creation.
    :param input_paths: The paths to the data in the datastore.
    :type input_paths: list of str
    :return: The formatted input paths.
    :rtype: dict of str, str

    Example usage:
    input_paths = format_input_mlt(["data.csv"])
    """
    input_paths_mlt = [{get_mlt_asset_type(path): path} for path in input_paths]

    return input_paths_mlt
