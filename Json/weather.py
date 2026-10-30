import requests

api_key = "ce3690063bb65266551b3f57f40e5543"

city = "Hubli"

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": api_key,
    "units": "metric"
}

response = requests.get(url, params=params)

print(response.status_code)

data = response.json()

print("City:", data["name"])
print("Temperature:", data["main"]["temp"], "°C")
print("Weather:", data["weather"][0]["description"])