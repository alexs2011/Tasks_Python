"""
Плоская структура
Структура данных в предыдущем задании — вложенные словари. Типичная задача разработчика — привести вложенные словари
к плоской структуре. А еще бывает полезно переложить список в словари для более удобного доступа по ключам.
Напишите функцию, которая сплющивает словарь с данными из предыдущего задания и раскладывает их в словарь,
где ключ — это pk.
"""

import json
from pprint import pprint as pp


def load_data(filename: str) -> list[dict]:
    with open(filename, 'r', encoding='utf-8') as f_in:
        return json.load(f_in)


def convert_data(data: list[dict]) -> dict[int:dict]:
    new_dict = {}
    for el in data:
        new_dict[el['pk']] = el['fields']
    return new_dict


if __name__ == '__main__':
    filename = 'data/cities.json'
    raw_data = load_data(filename)
    new_data = convert_data(raw_data)
    pp(new_data, indent=3)
