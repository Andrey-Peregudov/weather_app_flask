import request


def get_lan_lon(city_name, state_code, country_code, API_key):
    resp = request.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{state_code},{country_code}&appid={API_key}')