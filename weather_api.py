import requests
import configparser

# config.properties 파일에서 API_KEY와 CITY 읽어오기

# config.properties 파일에서 API_KEY 읽어오기
config = configparser.ConfigParser()
config.read('config.properties')

API_KEY = config.get('DEFAULT', 'API_KEY')  # API 키 읽어오기

BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"  # 5일치 날씨 데이터 API

# 날씨 데이터를 가져오는 함수 (5일치 날씨)
def fetch_weather(city_en, country_en):
    url = f"{BASE_URL}?q={city_en},{country_en}&appid={API_KEY}&units=metric&lang=kr"
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        print("Weather data:", weather_data)  # 전체 응답 데이터 출력

        # 5일치 날씨 데이터에서 평균 온도 계산
        temperatures = [entry['main']['temp'] for entry in weather_data['list']]
        print("Temperatures:", temperatures)  # 온도 값 출력

        avg_temp = int(sum(temperatures) / len(temperatures))
        print("Average Temperature:", avg_temp)  # 평균 온도 출력

        # 온도에 따른 옷 정보 결정
        if avg_temp <= 10:
            clothing_suggestion = "cold"
        elif 10 < avg_temp <= 30:
            clothing_suggestion = "average"
        else:
            clothing_suggestion = "hot"

        print(avg_temp)
        print(clothing_suggestion)
        
        return {
            'avg_temp': avg_temp,
            'clothing_suggestion': clothing_suggestion,
            'weather_data': weather_data
        }
    else:
        return None

# 날씨 데이터를 출력하는 함수
def print_weather_data(weather_data):
    if weather_data:
        print(f"5일치 날씨 예보: ")
        for entry in weather_data['list']:
            dt_txt = entry['dt_txt']  # 날짜/시간 정보
            temp = entry['main']['temp']  # 온도
            weather = entry['weather'][0]['description']  # 날씨 설명
            print(f"{dt_txt} - {temp}°C - {weather}")
    else:
        print("날씨 정보를 가져오지 못했습니다.")