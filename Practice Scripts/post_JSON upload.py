import json

import requests
import json

headers = {
    'Content-Type': 'application/json',
    'x-api-key': 'reqres-free-v1'
}

#payload = {
       # "first_name": "leo",
       # "last_name": "das",
#}

json_file = open("data.json")
data = json.load(json_file)

url="https://reqres.in//api/users"

response = requests.post(url,headers=headers,json=data)
print(response.status_code)
print(response.json())