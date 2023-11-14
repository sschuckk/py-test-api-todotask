import pytest
import requests
from requests import RequestException
import logging
from datetime import date
ENDPOINT = 'https://todo.pixegami.io'

# Set up the logger configuration
logging.basicConfig(filename=f'./py_test_api/logs/{date.today()}_Integration_api_methods_test.log',
                    format='%(asctime)s [%(levelname)8s] %(message)s (%(filename)s:%(funcName)s:%(lineno)s)',
                    level=logging.DEBUG,
                    force=True)

# Set logger to do the recording
logger = logging.getLogger(__name__)


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
    logger.info('Finishing testing...')
    pytest.exit('Done', returncode=0)
