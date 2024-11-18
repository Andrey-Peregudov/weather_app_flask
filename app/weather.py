import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')

def get_lan_lon(city_name, state_code, country_code, API_key):
    resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{state_code},{country_code}&appid={API_key}').json()
    print(resp)
get_lan_lon('Toronto', 'ON', "Canada", api_key)


