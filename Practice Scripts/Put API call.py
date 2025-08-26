import requests

head = {
    "accept": "text/plain",

}

response1 = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities/20",headers=head)
print("before update")
print(response1.json())


head1 = {
    "accept": "text/plain",
    "Content-Type": "application/json",
}

put_payload = {
  "id": 200,
  "title": "QAA",
  "dueDate": "2025-08-23T18:02:23.097Z",
  "completed": True
}

put_response = requests.put("https://fakerestapi.azurewebsites.net/api/v1/Activities/20",headers=head1,json=put_payload)
print("after update")
print(put_response.json())
print(put_response.status_code)









