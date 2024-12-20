import sqlite3

def initialize_database():
    # SQLite 데이터베이스 연결
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()

    # countries_cities_kr 테이블 생성 (한국어로 나라 및 도시명만 저장)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS countries_cities_kr (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        country_name_kr TEXT NOT NULL,
        city_name_kr TEXT NOT NULL
    )
    ''')

    # countries_cities_en 테이블 생성 (영어 데이터를 나중에 삽입할 예정)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS countries_cities_en (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        country_name_en TEXT NOT NULL,
        city_name_en TEXT NOT NULL,
        country_name_kr TEXT NOT NULL,
        city_name_kr TEXT NOT NULL
    )
    ''')

    # countries_cities_kr 초기 데이터 삽입 (한국어 나라, 도시명)
    cursor.executemany('''
    INSERT OR IGNORE INTO countries_cities_kr (country_name_kr, city_name_kr)
    VALUES (?, ?)
    ''', [
        ('러시아', '모스크바'),
        ('러시아', '상트페테르부르크'),
        ('노르웨이', '오슬로'),
        ('노르웨이', '베르겐'),
        ('베트남', '하노이'),
        ('베트남', '호찌민시'),
        ('한국', '서울'),
        ('한국', '부산'),
        ('중국', '베이징'),
        ('중국', '상하이'),
        ('몽골', '울란바토르'),
        ('몽골', '다르항'),
        ('스위스', '취리히'),
        ('스위스', '제네바')
    ])

    # countries_cities_en 초기 데이터 삽입 (한국어를 기준으로 영어 데이터 삽입)
    cursor.executemany('''
    INSERT OR IGNORE INTO countries_cities_en (country_name_en, city_name_en, country_name_kr, city_name_kr)
    VALUES (?, ?, ?, ?)
    ''', [
        ('Russia', 'Moscow', '러시아', '모스크바'),
        ('Russia', 'Saint Petersburg', '러시아', '상트페테르부르크'),
        ('Norway', 'Oslo', '노르웨이', '오슬로'),
        ('Norway', 'Bergen', '노르웨이', '베르겐'),
        ('Vietnam', 'Hanoi', '베트남', '하노이'),
        ('Vietnam', 'Ho Chi Minh City', '베트남', '호찌민시'),
        ('South Korea', 'Seoul', '한국', '서울'),
        ('South Korea', 'Busan', '한국', '부산'),
        ('China', 'Beijing', '중국', '베이징'),
        ('China', 'Shanghai', '중국', '상하이'),
        ('Mongolia', 'Ulaanbaatar', '몽골', '울란바토르'),
        ('Mongolia', 'Darkhan', '몽골', '다르항'),
        ('Switzerland', 'Zurich', '스위스', '취리히'),
        ('Switzerland', 'Geneva', '스위스', '제네바')
    ])

    # 변경사항 저장 및 연결 종료
    conn.commit()
    conn.close()
    print("Database initialized successfully.")

if __name__ == "__main__":
    initialize_database()