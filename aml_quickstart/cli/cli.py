# Created: 2024-07
# Created by: Basile El Azhari
# Maintained by: Basile El Azhari
# Contact: basile.elazhari@ekimetrics.com, https://www.linkedin.com/in/basile-el-azhari/

import click

from aml_quickstart.core.log import logger
from aml_quickstart.services.data.data import AmlDataService
from azure.ai.ml.constants import AssetTypes
from aml_quickstart.services.data.models import AMLFSOverwriteModeEnum

# Initialize the data service
data_service = AmlDataService()


@click.group()
def cli():
    """CLI for Azure Machine Learning Data Service"""
    pass


# ## Data Service Commands ## #


@cli.command()
def create_or_update_adls_datastore():
    """Create or update an ADLS Gen2 datastore in Azure ML"""
    try:
        store = data_service.create_or_update_adls_gen2_datastore()
        click.echo(f"ADLS Gen2 Datastore created/updated: {store.name}")
    except Exception as e:
        click.echo(f"Error: {e}")


@cli.command()
@click.argument("input_paths", nargs=-1, type=click.STRING)
@click.argument("mltable-save-path", nargs=1, type=click.STRING)
@click.option(
    "--inputs-extension",
    default="csv",
    help="Extension of the input files (csv, parquet, json).",
    type=click.STRING,
)
@click.option(
    "--headers",
    default="all_files_same_headers",
    help="Headers for the mltable.",
    type=click.STRING,
)
@click.option(
    "--data-description",
    default=None,
    help="Description of the mltable.",
    type=click.STRING,
)
@click.option(
    "--data-version", default=None, help="Version of the mltable.", type=click.STRING
)
@click.option(
    "--infer-column-types",
    is_flag=True,
    default=True,
    help="Infer column types.",
    type=click.BOOL,
)
@click.option(
    "--include-path-column",
    is_flag=True,
    default=False,
    help="Include path column.",
    type=click.BOOL,
)
@click.option(
    "--keep-columns",
    default=None,
    help="Columns to keep (comma-separated).",
    type=click.STRING,
)
@click.option(
    "--drop-columns",
    default=None,
    help="Columns to drop (comma-separated).",
    type=click.STRING,
)
@click.option(
    "--filter-lines",
    default=None,
    help="Filter lines in mltable (pyspark.sql format).",
    type=click.STRING,
)
def create_mltable(
    input_paths: list[str],
    mltable_save_path: str,
    inputs_extension: str = "csv",
    headers: str = "all_files_same_headers",
    data_description: str | None = None,
    data_version: str | None = None,
    infer_column_types: bool = True,
    include_path_column: bool = False,
    keep_columns: str | None = None,
    drop_columns: str | None = None,
    filter_lines: str | None = None,
):
    """Create a mltable from input paths like '[{"file": "wasbs://data@azuremlexampledata.blob.core.windows.net/titanic.csv"}]'"""

    # Parsing arguments

    keep_columns_list = keep_columns.split(",") if keep_columns else []
    drop_columns_list = drop_columns.split(",") if drop_columns else []

    logger.info(f"Creating MLTable with input paths: {input_paths}")

    data_service.create_mltable(
        input_paths=input_paths,
        mltable_save_path=mltable_save_path,
        inputs_extension=inputs_extension,
        headers=headers,
        data_description=data_description,  # type: ignore
        data_version=data_version,
        infer_column_types=infer_column_types,
        include_path_column=include_path_column,
        keep_columns=keep_columns_list,
        drop_columns=drop_columns_list,
        filter_lines=filter_lines,
    )
    logger.info("MLTable created successfully")


@cli.command()
@click.argument("path", type=click.STRING)
@click.option(
    "--asset-type",
    default=AssetTypes.URI_FILE,
    help="Asset type (uri_file, uri_folder, mltable).",
    type=click.STRING,
)
@click.option(
    "--data-description",
    default=None,
    help="Description of the dataset.",
    type=click.STRING,
)
@click.option(
    "--data-name", default=None, help="Name of the dataset.", type=click.STRING
)
@click.option(
    "--data-version", default=None, help="Version of the dataset.", type=click.STRING
)
def create_dataset(
    path: str,
    asset_type: str = AssetTypes.URI_FILE,
    data_description: str | None = None,
    data_name: str | None = None,
    data_version: str | None = None,
):
    """Create a dataset in Azure ML"""
    data_service.create_dataset(
        path=path,
        asset_type=asset_type,
        data_description=data_description,
        data_name=data_name,
        data_version=data_version,
    )
    click.echo(f"Dataset created successfully: {data_name}")


@cli.command()
@click.option(
    "--mltable-name", default=None, help="Name of the mltable.", type=click.STRING
)
@click.option(
    "--mltable-version", default=None, help="Version of the mltable.", type=click.STRING
)
@click.option(
    "--path",
    default=None,
    help="Path to the file or folder in the datastore.",
    type=click.STRING,
)
@click.option(
    "--data-source",
    default="local",
    help="Source of the data (datastore, databricks, local).",
    type=click.STRING,
)
@click.option(
    "--data-features",
    default=None,
    help="Features to keep in the DataFrame (comma-separated).",
    type=click.STRING,
)
def get_dataframe(
    mltable_name: str | None = None,
    mltable_version: str | None = None,
    path: str | None = None,
    data_source: str = "local",
    data_features: str | None = None,
):
    """Get a Pandas DataFrame from a mltable, file, or folder"""
    data_features_list = data_features.split(",") if data_features else None
    df = data_service.get_dataframe(
        mltable_name=mltable_name,
        mltable_version=mltable_version,
        path=path,
        data_source=data_source,
        data_features=data_features_list,
    )
    click.echo(f"DataFrame loaded with {len(df)} rows and {len(df.columns)} columns.")


@cli.command()
@click.argument("path", type=click.STRING)
@click.option(
    "--data-source",
    default="local",
    help="Source of the data (datastore, databricks, local).",
    type=click.STRING,
)
def get_uri(path: str, data_source: str = "local"):
    """Get the URI of a file in the datastore or Databricks"""
    uri = data_service.get_uri(path, data_source=data_source)
    click.echo(f"File URI: {uri}")


@cli.command()
@click.argument("source-path", type=click.STRING)
@click.argument("dest-path", type=click.STRING)
@click.option(
    "--asset-type",
    default=AssetTypes.URI_FILE,
    help="Type of asset to upload (uri_file, uri_folder, mltable).",
)
@click.option(
    "--overwrite",
    default="overwrite",
    help="Overwrite mode (overwrite, append, fail_on_file_conflict).",
)
def upload_file_to_datastore(
    source_path: str,
    dest_path: str,
    asset_type: str = AssetTypes.URI_FILE,
    overwrite: str = AMLFSOverwriteModeEnum.overwrite,
):
    """Upload a file to the datastore"""
    uri = data_service.upload_file_to_datastore(
        source_path=source_path,
        dest_path=dest_path,
        asset_type=asset_type,
        overwrite=overwrite,
    )
    click.echo(f"File uploaded successfully to: {uri}")


#
# @cli.command()
# @click.argument("source-path", type=click.STRING)
# @click.argument("dest-path", type=click.STRING)
# @click.option(
#     "--asset-type",
#     default=AssetTypes.URI_FILE,
#     help="Type of asset to download (uri_file, uri_folder, mltable).",
# )
# @click.option(
#     "--overwrite",
#     default="overwrite",
#     help="Overwrite mode (overwrite, append, fail_on_file_conflict).",
# )
# def download_file_from_datastore(
#     source_path: str,
#     dest_path: str,
#     asset_type: str = AssetTypes.URI_FILE,
#     overwrite: str = AMLFSOverwriteModeEnum.overwrite,
# ):
#     """Download a file from the datastore to the local machine"""
#     local_path = data_service.down(
#         source_path=source_path,
#         dest_path=dest_path,
#         asset_type=asset_type,
#         overwrite=overwrite,
#     )
#     click.echo(f"File downloaded successfully to: {local_path}")
