# All settings are stored in the Settings class. Values are read from environment variables or a .env file.
# Created: 2024-07
# Created by: Basile El Azhari
# Maintained by: Basile El Azhari
# Contact: basile.elazhari@ekimetrics.com, https://www.linkedin.com/in/basile-el-azhari/

import os
import pytest
from click.testing import CliRunner
from ezazml.cli.cli import cli

from ezazml.core.log import logger


@pytest.fixture
def runner():
    return CliRunner()


@pytest.fixture
def data_path():
    return "integration/data/books.csv"


@pytest.fixture
def temp_folder():
    yield "temp/"
    os.system('rm -rf "tests/temp/"')


def test_create_or_update_adls_datastore(runner):
    result = runner.invoke(cli, ["create-or-update-adls-datastore"])

    logger.info(result.output)
    assert "ADLS Gen2 Datastore created/updated" in result.output
    assert result.exit_code == 0


def test_create_mltable(runner, temp_folder):
    input_paths = "wasbs://data@azuremlexampledata.blob.core.windows.net/titanic.csv"
    mltable_save_path = f"{temp_folder}titanic_mlt"

    result = runner.invoke(
        cli,
        [
            "create-mltable",
            input_paths,
            mltable_save_path,
            "--inputs-extension=csv",
            "--headers=all_files_same_headers",
            "--infer-column-types",
            "--include-path-column",
            "--keep-columns=col1,col2",
            "--drop-columns=col3",
        ],
    )
    logger.info(result.output)
    assert result.exit_code == 0


def test_create_dataset(runner, data_path):
    result = runner.invoke(
        cli,
        [
            "create-dataset",
            data_path,
            "--asset-type=uri_file",
            '--data-description="Dataset Description"',
            "--data-name=DatasetName",
        ],
    )

    logger.info(result.output)
    assert result.exit_code == 0


def test_get_dataframe(runner, data_path):
    result = runner.invoke(
        cli, ["get-dataframe", f"--path={data_path}", "--data-source=local"]
    )

    logger.info(result.output)
    assert result.exit_code == 0


def test_get_uri(runner, data_path):
    result = runner.invoke(cli, ["get-uri", data_path, "--data-source=local"])

    logger.info(result.output)
    assert result.exit_code == 0

    result = runner.invoke(cli, ["get-uri", data_path, "--data-source=datastore"])

    logger.info(result.output)
    assert result.exit_code == 0


def test_upload_file_to_datastore(runner, data_path, temp_folder):
    result = runner.invoke(
        cli,
        [
            "upload-file-to-datastore",
            data_path,
            temp_folder,
            "--asset-type",
            "uri_file",
            "--overwrite",
            "MERGE_WITH_OVERWRITE",
        ],
    )

    logger.info(result.output)
    assert result.exit_code == 0


# def test_download_file_from_datastore(runner, data_path, temp_folder):
#     result = runner.invoke(
#         cli,
#         [
#             'download-file-from-datastore',
#             f'{temp_folder}books.csv',
#             f'{temp_folder}downloaded_books.csv',
#         ]
#     )
#
#     print(result.output)
#     assert result.exit_code == 0
