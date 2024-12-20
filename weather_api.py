import requests
import configparser

# config.properties 파일에서 API_KEY와 CITY 읽어오기

config = configparser.ConfigParser()
config.read('config.properties')

API_KEY = config.get('DEFAULT', 'API_KEY')

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# 날씨 데이터를 가져오는 함수
def fetch_weather(city_en, country_en):
    url = f"{BASE_URL}?q={city_en},{country_en}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # JSON 데이터 반환
    else:
        return None  # 실패 시 None 반환