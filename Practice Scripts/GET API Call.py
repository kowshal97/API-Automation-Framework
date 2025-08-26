import requests

head = {
    "accept": "text/plain"
}

response = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities", headers = head)

print(response.status_code)
print(response.json())

response1 = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities/6")
print(response1.status_code)
print(response1.json())

assert response1.status_code == 200
assert response.status_code == 200