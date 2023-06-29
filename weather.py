import os

import requests
from dotenv import load_dotenv


def get_weather(city):
    load_dotenv()
    request_link = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv("WEATHER_TOKEN")}'
    response = requests.get(request_link).json()
    weather = {
        'weather_description': response['weather'][0]['description'],
        'temperature': round(response['main']['temp'] - 273),
        'humidity': response['main']['humidity']
    }

    return weather
