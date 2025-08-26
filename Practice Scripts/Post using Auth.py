import requests

head = {
    "content-type": "application/json",
    "authorization": "Bearer aef9d049b280655a5c8f792e883751e1369b4d5d747891267377635b027b80fb"
}

payload = {
  "name": "leo",
  "email": "leodas123121313f892824r78@gmail.com",
  "gender": "male",
  "status": "active"
}

url = 'https://gorest.co.in/public/v2/users'

response = requests.post(url,headers=head,json=payload)
print(response.status_code)
print(response.json())
assert response.status_code == 201

getresponse = requests.get(url+'/'+str(response.json()["id"]),headers=head)
print(getresponse.json())



