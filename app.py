from flask import Flask, render_template, request, jsonify
from database import get_countries, get_cities, get_english_name, get_basic_items  # get_basic_items 함수 추가
from weather_api import fetch_weather

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
    selected_country = None
    selected_city = None
    weather_data = None
    error = None
    cities = []

    if request.method == 'POST':
        selected_country = request.form.get('country')
        selected_city = request.form.get('city')

        # 국가가 선택되었으면 도시 목록 가져오기
        if selected_country:
            cities = get_cities(selected_country)

        # 도시와 국가가 모두 선택되었으면 날씨 정보 가져오기
        if selected_country and selected_city:
            weather_data, error = fetch_weather_data(selected_country, selected_city)

    # 국가 목록 가져오기
    countries = get_countries()

    return render_template(
        'index.html',
        countries=countries,
        cities=cities,
        selected_country=selected_country,
        selected_city=selected_city,
        weather_data=weather_data,
        error=error
    )

# 도시 목록 API 라우트
@app.route('/get_cities')
def get_cities_route():
    country = request.args.get('country')
    if country:
        cities = get_cities(country)
        return jsonify({'cities': cities})
    return jsonify({'error': '국가를 선택해주세요.'})

# 날씨 정보 API 라우트
@app.route('/get_weather')
def get_weather_route():
    print("get_weather_route called")  # 라우트 호출 로그 확인

    country = request.args.get('country')
    city = request.args.get('city')

    if not country or not city:
        return jsonify({'error': '국가와 도시를 모두 선택해주세요.'})

    weather_data, error = fetch_weather_data(country, city)  # 두 값을 언팩
    print("Fetched weather data:", weather_data)  # 응답 데이터 확인용 출력

    if error:  # error가 있으면 오류 메시지 반환
        return jsonify({'error': error})

    return jsonify({'weather': weather_data})  # 날씨 정보 반환

# 날씨 페이지 라우트
@app.route('/weather.html', methods=['GET'])
def weather():
    country = request.args.get('country')
    city = request.args.get('city')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    gender = request.args.get('gender')

    if not country or not city:
        return render_template('weather.html', error="국가와 도시를 선택해주세요.")

    weather_data, error = fetch_weather_data(country, city)
    if error:
        return render_template('weather.html', error=error)

    return render_template(
        'weather.html',
        country=country,
        city=city,
        start_date=start_date,
        end_date=end_date,
        gender=gender,
        weather_data=weather_data
    )
def fetch_weather_data(country, city):
    english_name = get_english_name(country, city)

    if not english_name:
        return None, "영어 이름을 가져올 수 없습니다."

    city_en, country_en = english_name['city_name_en'], english_name['country_name_en']

    weather_data = fetch_weather(city_en, country_en)

    if weather_data:
        return weather_data, None
    else:
        return None, "날씨 데이터를 가져올 수 없습니다."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3012, debug=True)