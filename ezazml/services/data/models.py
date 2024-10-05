# Created: 2024-07
# Created by: Basile El Azhari
# Maintained by: Basile El Azhari
# Contact: basile.elazhari@ekimetrics.com, https://www.linkedin.com/in/basile-el-azhari/

from enum import Enum

import pandas as pd


class AzureMLTablesAssetTypesEnum(str, Enum):
    FILE: str = "file"
    FOLDER: str = "folder"
    PATTERN: str = "pattern"


class AMLFSOverwriteModeEnum(str, Enum):
    overwrite: str = "MERGE_WITH_OVERWRITE"
    append: str = "APPEND"
    fail: str = "FAIL_ON_FILE_CONFLICT"


class DataSourceEnum(str, Enum):
    local: str = "local"
    datastore: str = "datastore"
    databricks: str = "databricks"


class MltFromTypeEnum(str, Enum):
    csv: str = "csv"
    parquet: str = "parquet"
    json: str = "json"
    delta_lake: str = "delta_lake"


PANDAS_READ_MAPPING = {
    "parquet": pd.read_parquet,
    "csv": pd.read_csv,
    "json": pd.read_json,
}
