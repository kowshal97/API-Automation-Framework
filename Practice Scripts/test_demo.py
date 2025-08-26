import requests
import pytest

def test_demo():
    headers = {
        "Content-Type":"application/json",
        "api-key":"reqres-free-v1",
    }
    base_url = "https://reqres.in"
    response = requests.get(base_url+ "/api/users/2", headers=headers)
    assert response.status_code == 200
    print(response.json())
    print(response.text)