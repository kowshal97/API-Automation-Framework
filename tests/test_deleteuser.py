import uuid
import pytest
from utils.apis import APIS

@pytest.fixture(scope='module')
def apis():
    return APIS()


def test_delete_user_validation(apis):
    response = apis.delete('users/3')
    print(response.json())
    assert response.status_code == 404