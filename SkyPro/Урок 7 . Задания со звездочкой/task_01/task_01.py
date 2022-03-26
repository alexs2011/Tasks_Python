"""
Группировка городов
Работаем с частью сервиса, связанного с городами.
Пройдите список словарей, сгруппируйте города по странам и выведите их.
"""
import json


def load_data(filename: str) -> list[dict]:
    with open(filename, 'r', encoding='utf-8') as f_in:
        return json.load(f_in)


def group_by_country(cities: list[dict]) -> dict:
    countries = {}
    for el in cities:
        data = el['fields']
        countries[data['country_ru']] = countries.setdefault(data['country_ru'], [])
        countries[data['country_ru']].append(data['name'])
    return countries


if __name__ == '__main__':
    filename = 'data/cities.json'
    cities = load_data(filename)
    res = group_by_country(cities)
    for country, cities_lst in res.items():
        print(f'{country}:')
        for city in cities_lst:
            print(f'- {city}')
        print()
