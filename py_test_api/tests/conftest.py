import pytest
import requests
from requests import RequestException
import logging

logger = logging.getLogger(__name__)
ENDPOINT = 'https://todo.pixegami.io'


@pytest.fixture(autouse=True, scope="module")
def verify_endpoint() -> None:
    """
    Fixture function for verifying the connection to an endpoint.

    This fixture sends a GET request to the specified endpoint and asserts
    that the response status code is 200, indicating a successful connection.
    """
    try:
        logger.info('Verifying endpoint connection...')
        response = requests.get(ENDPOINT)
        assert response.status_code == 200
    except RequestException as e:
        logger.error(f'Endpoint connection failed, due to exception: {e}')
        pytest.exit('Execution Error', returncode=3)

    yield
    logger.info('Exiting testing...')
    pytest.exit('Done', returncode=0)
