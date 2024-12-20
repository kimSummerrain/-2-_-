import sqlite3

# DB 연결 함수
def get_db_connection():
    conn = sqlite3.connect('weather.db')
    conn.row_factory = sqlite3.Row  # 반환되는 데이터가 dict 형태로 반환되도록 설정
    return conn

# 국가 목록을 가져오는 함수
def get_countries():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT country_name_kr FROM countries_cities_kr')
    countries = cursor.fetchall()
    conn.close()
    return [{'country_name_kr': country['country_name_kr']} for country in countries]

# 선택된 국가에 해당하는 도시 목록을 가져오는 함수
def get_cities(country_name_kr):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT city_name_kr FROM countries_cities_kr WHERE country_name_kr = ?', (country_name_kr,))
    cities = cursor.fetchall()
    conn.close()
    return [{'city_name_kr': city['city_name_kr']} for city in cities]

# 한국어 국가명과 도시명으로 영어명 가져오기
def get_english_name(country_name_kr, city_name_kr):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT country_name_en, city_name_en 
        FROM countries_cities_en
        WHERE country_name_kr = ? AND city_name_kr = ?
    ''', (country_name_kr, city_name_kr))
    data = cursor.fetchone()
    conn.close()
    return {'country_name_en': data[0], 'city_name_en': data[1]} if data else None