import requests

# defining the api-endpoint
API_ENDPOINT = "https://reqres.in/api/register"

data = {'email': 'kushan@lk.lk',
        'password': 'kushan'}

r = requests.post(url=API_ENDPOINT, data=data)

print(r.status_code)
print(r.json())
assert  r.status_code == 201