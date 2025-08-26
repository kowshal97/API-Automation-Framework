import requests

head = {
    "accept": "text/plain",
    "content-type": "application/json",
}

payload = {
  "id": 31,
  "idBook": 2,
  "firstName": "leo",
  "lastName": "das"
}

response = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Authors",headers = head, json=payload)
data = response.json()
print(data["id"])

print(response.json())
print(response.status_code)

assert response.status_code == 200
assert data["id"] == 31