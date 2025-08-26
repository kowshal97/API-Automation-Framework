import uuid
import pytest
from utils.apis import APIS

@pytest.fixture(scope='module')
def apis():
    return APIS()

def test_update_user_validation(apis):
    user_data = {
        "name" : "leokowshal",
        'Email': 'Shanna232@melissa.tv',
        'phone': '010-6922-6593 x09125',
    }
    response = apis.put('users/2',user_data)
    print(response.json())
    assert response.status_code == 404