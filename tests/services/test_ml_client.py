import pytest
from unittest.mock import patch, MagicMock

# Assuming the module name is `ml_client_module` and it's located in the same directory
from aml_quickstart.services.ml_client import get_ml_client


@pytest.fixture
def mock_settings():
    with patch("aml_quickstart.core.settings.get_settings") as mock_get_settings:
        # Mock the settings with the necessary attributes
        mock_settings_instance = MagicMock()
        mock_settings_instance.aml.AML_SUBSCRIPTION_ID = "fake_subscription_id"
        mock_settings_instance.aml.AML_RESOURCE_GROUP = "fake_resource_group"
        mock_settings_instance.aml.AML_WORKSPACE_NAME = "fake_workspace_name"

        mock_get_settings.return_value = mock_settings_instance
        yield mock_get_settings


@pytest.fixture
def mock_default_azure_credential():
    with patch("azure.identity.DefaultAzureCredential") as mock_credential:
        yield mock_credential


@pytest.fixture
def mock_ml_client():
    with patch("azure.ai.ml.MLClient") as mock_client:
        yield mock_client


def test_get_ml_client(mock_settings, mock_default_azure_credential, mock_ml_client):
    # Call the function to test
    client = get_ml_client()

    # Assertions to ensure the function behaves as expected
    mock_ml_client.assert_called_once_with(
        mock_default_azure_credential.return_value,
        mock_settings.return_value.aml.AML_SUBSCRIPTION_ID,
        mock_settings.return_value.aml.AML_RESOURCE_GROUP,
        mock_settings.return_value.aml.AML_WORKSPACE_NAME,
    )

    assert client == mock_ml_client.return_value
