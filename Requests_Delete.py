import requests

API_ENDPOINT = "https://reqres.in/api/users/2"

r = requests.delete(API_ENDPOINT)

print(r.status_code)

assert r.status_code == 204

