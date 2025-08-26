import uuid
import pytest
from utils.apis import APIS

@pytest.fixture(scope='module')
def apis():
    return APIS()

def test_createuser_validation(apis,load_user_data):
   # user_data = {
    #    "name": "leo",
    #    "last_name": "das",
     #   "role": "admin",
     #   "email": "leodas@gmail.com",
   # }
    user_data = load_user_data["new_user"]
    unique_email = f"{uuid.uuid4().hex[:8]}@gmail.com"
    print(unique_email)
    user_data["email"] = unique_email
    response = apis.post('users',user_data)
    print(response.json())
    assert response.status_code == 201
    assert response.json()["name"] == load_user_data["new_user"]["name"]
    id = response.json()['id']
    responseget = apis.get('users/10')
    print(responseget.json())
    assert responseget.status_code == 200
    assert responseget.json()['name']=="Clementina DuBuque"