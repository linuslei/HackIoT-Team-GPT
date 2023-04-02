import requests
import json

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        return data["weather"][0]["main"]
    else:
        print("Failed to fetch weather data")
        return None