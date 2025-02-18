import requests
import pytest

from config.env_vars import EnVariables


@pytest.fixture(autouse=True, scope="session")
def init_environment():
    response = requests.post(
        url=f"{EnVariables.HOST}/setup",
        headers={"TOKEN": f"{EnVariables.API_TOKEN}"}
    )

    assert response.status_code == 202
