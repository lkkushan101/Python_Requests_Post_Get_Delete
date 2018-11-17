import requests
import json
r = requests.get('http://restapi.demoqa.com/utilities/weather/city/Pune')
print(r.text)
print(r.status_code)
assert r.status_code == 200
data = json.loads(r.content)
assert data['City'] == "Pune"
assert data['Humidity'] == "30 Percent"
assert data['Humidity'] == "30 Percent"
assert data['WeatherDescription'] == "clear sky"