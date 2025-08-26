import uuid
import pytest
from utils.apis import APIS

@pytest.fixture(scope='module')
def apis():
    return APIS()


def test_getoneuser_validation(apis):
    response = apis.get("users/2")
    print(response.json())
    assert response.status_code == 200