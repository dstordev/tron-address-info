import pytest
from starlette.testclient import TestClient

from src.app import app


@pytest.mark.asyncio(loop_scope="function")
def test_on_address_info():
    address = "TNPdqto8HiuMzoG7Vv9wyyYhWzCojLeHAF"

    with TestClient(app) as client:
        response = client.post(f"{client.base_url}/address/info",
                               json={"address": address})

        assert response.status_code == 200

        response_data = response.json()
        assert isinstance(response_data, dict)
        assert set(response_data.keys()) == {'bandwidth', 'balance', 'energy'}
