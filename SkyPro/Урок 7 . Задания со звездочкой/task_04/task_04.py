"""
https://skyengpublic.notion.site/7-926058c7c84d4c879487573427fe3dc1
Пересечения
Вам предоставлен набор множеств. Запишите их в удобном формате.
Напишите программу, которая выведет все возможные сочетания множеств.
Затем программа должна вывести инверсию для каждого множества (рыба не входит в это множество, но входит в остальные).
"""

import json
from json import JSONEncoder


# subclass JSONEncoder
class setEncoder(JSONEncoder):
    def default(self, obj):
        return list(obj)


def load_data(filename: str) -> list[dict]:
    with open(filename, 'r', encoding='utf-8') as f_in:
        data = json.load(f_in)
        for el in data:
            for key, val in el.items():
                el[key] = set(val)
    return data


def find_all_intersections(data: list[dict]) -> dict:
    res = {}
    for i, prop_1 in enumerate(data):
        for prop_2 in data[i + 1:]:
            key_1, key_2 = *prop_1.keys(), *prop_2.keys()
            val_1, val_2 = *prop_1.values(), *prop_2.values()
            res[f'{key_1} и {key_2}'] = val_1.intersection(val_2)
    return res


def find_inversions(data: list[dict]) -> dict:
    res = {}
    total_fishes_set = set()
    sets_lst = [val for prop in data for val in prop.values()]
    for s in sets_lst:
        total_fishes_set.update(s)

    for prop in data:
        for key, val in prop.items():
            res[f"Не {key}"] = total_fishes_set.difference(val)
    return res


def save_data(data: dict, filename: str) -> None:
    with open(filename, 'w', encoding='utf-8') as f_out:
        json.dump(data, f_out, ensure_ascii=False, cls=setEncoder, indent=3)


if __name__ == '__main__':
    filename = 'data/fishes.json'
    fishes_properties = load_data(filename)

    all_intersections = find_all_intersections(fishes_properties)

    save_data(all_intersections, 'data/intersections.json')

    # for key, val in all_intersections.items():
    #     print(f"{key}:")
    #     for fish in val:
    #         print(fish)
    #     print()

    inversions = find_inversions(fishes_properties)

    save_data(inversions, 'data/inversions.json')

    # for key, val in inversions.items():
    #     print(f"{key}:")
    #     for fish in val:
    #         print(fish)
    #     print()
