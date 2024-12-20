from flask import Flask, render_template, request, jsonify
from database import get_countries, get_cities, get_english_name
from weather_api import fetch_weather

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    selected_country = None
    selected_city = None
    weather_data = None
    error = None
    cities = []

    # 국가 선택 후, 해당 국가의 도시 목록 가져오기
    if request.method == 'POST':
        selected_country = request.form['country']
        selected_city = request.form['city']
        cities = get_cities(selected_country)  # 선택된 국가의 도시 목록 가져오기

        # 도시 정보가 제공되면 날씨 데이터를 가져옵니다.
        if selected_city:
            english_name = get_english_name(selected_country, selected_city)
            if english_name:
                country_en, city_en = english_name
                weather_data = fetch_weather(city_en, country_en)
            else:
                error = "Invalid city name in database."

    countries = get_countries()  # 국가 목록 가져오기
    return render_template('index.html', 
                           countries=countries, 
                           cities=cities, 
                           selected_country=selected_country,
                           selected_city=selected_city, 
                           weather_data=weather_data, 
                           error=error)

# 국가에 해당하는 도시 목록을 JSON 형식으로 반환하는 라우트
@app.route('/get_cities')
def get_cities_route():
    country = request.args.get('country')
    cities = get_cities(country)
    return jsonify({'cities': cities})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3012, debug=True)