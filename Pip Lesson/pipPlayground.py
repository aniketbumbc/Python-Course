# install pckgs
# python3 -m pip install requests
#  python3 -m pip list
# specific pckg  python3 -m pip installl requests==2.30.0
# uninstall ###  python3 pip uninstall requests
# Activate virtual env source .venv/bin/activate
# Deactivate deactivate


import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()


def current_weather():
    print("\n**** Get current weather conditions ****\n")
    city = input("\n Please enter city name: \n")
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={
        os.getenv("API_KEY")}&q={city}&units=metric'

    weather_data = requests.get(request_url).json()
    pprint(weather_data)


current_weather()
