# All settings are stored in the Settings class. Values are read from environment variables or a .env file.
# Created: 2024-07
# Created by: Basile El Azhari
# Maintained by: Basile El Azhari
# Contact: basile.elazhari@ekimetrics.com, https://www.linkedin.com/in/basile-el-azhari/

from azure.ai.ml import command, Input, Output, MLClient
from azure.ai.ml.constants import AssetTypes, InputOutputModes

from ezazml.services.ml_client import get_ml_client
from ezazml.services.data.data import AmlDataService


class DataJob:
    """
    Data job class.


    Example usage:
    data_uri = AmlDataService().get_data_uri()
    data_job = DataJob(ml_client, data_uri, asset_type=AssetTypes.URI_FILE, mode=InputOutputModes.RO_MOUNT)
    data = data_job.run_ingestion_monitoring(run_job_monitoring=True)
    """

    def __init__(self, identity=None):
        self.ml_client: MLClient = get_ml_client()
        self.identity = identity  # TODO : Add identity management
        # https://learn.microsoft.com/en-us/azure/machine-learning/how-to-read-write-data-v2?view=azureml-api-2&tabs=python#read-data-from-azure-storage-in-an-azure-machine-learning-job

    def create_or_update_adls_gen2_datastore(self) -> int:
        """
        Create or update the ADLS Gen2 datastore.
        """
        ads = AmlDataService()
        ads.create_or_update_adls_gen2_datastore()
        return 0

    def run_copy(
        self,
        input_data_uri: str,
        output_data_uri: str,
        register_dataset_name: str | None = None,
        register_dataset_version: str | None = None,
        input_asset_type: AssetTypes | str = AssetTypes.URI_FILE,
        input_io_mode: InputOutputModes = InputOutputModes.RO_MOUNT,
        output_asset_type: AssetTypes | str = AssetTypes.URI_FILE,
        output_io_mode: InputOutputModes = InputOutputModes.RW_MOUNT,
    ) -> str:
        """
        Run the data job. Used to copy data from the input path to the output path. Returns the job ID.
        :param input_data_uri: The input data URI.
        :type input_data_uri: str
        :param output_data_uri: The output data URI.
        :type output_data_uri: str
        :param register_dataset_name: The dataset name to register. Default is None, and no dataset is registered.
        :type register_dataset_name: str | None
        :param register_dataset_version: The dataset version to register. Default is None, and no dataset is registered.
        :type register_dataset_version: str | None
        :param input_asset_type: The asset type. Default is AssetTypes.URI_FILE. Other options are AssetTypes.URI_FOLDER, AssetTypes.URI_PATTERN.
        :type input_asset_type: AssetTypes | str
        :param input_io_mode: The input/output mode InputOutputModes.RO_MOUNT or InputOutputModes.RW_MOUNT for landing data.
        :type input_io_mode: InputOutputModes
        :param output_asset_type: The asset type. Default is AssetTypes.URI_FILE. Other options are AssetTypes.URI_FOLDER, AssetTypes.URI_PATTERN.
        :type output_asset_type: AssetTypes | str
        :param output_io_mode: The input/output mode InputOutputModes.RO_MOUNT or InputOutputModes.RW_MOUNT for landing data.
        :type output_io_mode: InputOutputModes
        :return: The job ID.
        :rtype: str
        :raises ValueError: If register_dataset_name is provided without register_dataset_version.

        Example usage:
        input_data_uri = AmlDataService().get_data_uri()
        data_job = DataJob(ml_client, data_uri, asset_type=AssetTypes.URI_FILE, mode=InputOutputModes.RO_MOUNT)
        job = data_job.run_io()
        """
        # Inputs
        inputs = {
            "input_data": Input(
                type=str(input_asset_type),
                path=str(input_data_uri),
                mode=str(input_io_mode),
            )
        }

        # Outputs
        if (register_dataset_name is not None) and (register_dataset_version is None):
            raise ValueError(
                "register_dataset_name and register_dataset_version must be provided together."
            )
        if (register_dataset_name is not None) and (
            register_dataset_version is not None
        ):
            outputs = {
                "output_data": Output(
                    type=str(output_asset_type),
                    path=str(output_data_uri),
                    mode=str(output_io_mode),
                    name=register_dataset_name,
                    version=register_dataset_version,
                )
            }
        else:
            outputs = {
                "output_data": Output(
                    type=str(output_asset_type),
                    path=str(output_data_uri),
                    mode=str(output_io_mode),
                )
            }

        # Command
        job_io = command(
            command="cp ${{inputs.input_data}} ${{outputs.output_data}}",
            inputs=inputs,
            outputs=outputs,
            environment="azureml://registries/azureml/environments/sklearn-1.1/versions/4",
            compute="cpu-cluster",
            identity=self.identity,
        )

        return self.ml_client.jobs.create_or_update(job_io)

    def run_show_mlt_paths(
        self,
        mlt_name: str,
        mlt_version: str,
        io_mode: InputOutputModes = InputOutputModes.EVAL_MOUNT,
    ) -> str:
        """
        Run the data job. Used to show the paths of the dataset. Returns the job ID.
        :param mlt_name: The dataset name.
        :type mlt_name: str
        :param mlt_version: The dataset version.
        :type mlt_version: str
        :param io_mode: The input/output mode Default is InputOutputModes.EVAL_MOUNT. Other option is InputOutputModes.EVAL_DOWNLOAD
        :type io_mode: InputOutputModes
        :return: The job ID.
        :rtype: str

        Example usage:
        data_job = DataJob(ml_client)
        job = data_job.run_show_mltable_paths("my_dataset")
        """
        mlt = self.ml_client.data.get(name=mlt_name, version=mlt_version)
        inputs = {
            "input_data": Input(type=AssetTypes.MLTABLE, path=mlt.id, mode=io_mode)
        }

        cmd = "ls ${{inputs.input_data}}/**"
        job_io = command(
            command=cmd,
            inputs=inputs,
            environment="azureml://registries/azureml/environments/sklearn-1.1/versions/4",
            compute="cpu-cluster",
        )

        return self.ml_client.jobs.create_or_update(job_io)

    def run_show_mlt_head(
        self,
        mlt_name: str,
        mlt_version: str,
        io_mode: InputOutputModes = InputOutputModes.EVAL_MOUNT,
    ) -> str:
        """
        Run the data job. Used to show the head of the dataset. Returns the job ID.
        :param mlt_name: The dataset name.
        :type mlt_name: str
        :param mlt_version: The dataset version.
        :type mlt_version: str
        :param io_mode: The input/output mode Default is InputOutputModes.EVAL_MOUNT. Other option is InputOutputModes.EVAL_DOWNLOAD
        :type io_mode: InputOutputModes
        :return: The job ID.
        :rtype: str

        Example usage:
        data_job = DataJob(ml_client)
        job = data_job.run_show_head("my_dataset")
        """
        mlt = self.ml_client.data.get(name=mlt_name, version=mlt_version)
        inputs = {
            "input_data": Input(type=AssetTypes.MLTABLE, path=mlt.id, mode=io_mode)
        }

        cmd = "head ${{inputs.input_data}}"
        job_io = command(
            command=cmd,
            inputs=inputs,
            environment="azureml://registries/azureml/environments/sklearn-1.1/versions/4",
            compute="cpu-cluster",
        )

        return self.ml_client.jobs.create_or_update(job_io)
