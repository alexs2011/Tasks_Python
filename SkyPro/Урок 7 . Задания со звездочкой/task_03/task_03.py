"""
Отображение
Перевод данных из одной системы ключей в другую — рутинная и не всегда приятная задача. Давайте автоматизируем ее!
Напишите функцию, которая принимает на вход первым аргументом список словарей, а вторым — словарь соответствия ключей.
Например:
f   surname
i   name
o   patronymic
Пример такого словаря:
data_map = {"f": "surname", "i": "name", "o": "patronymic"}
"""


def mapper(data: dict, data_map: dict) -> dict:
    mapped_data = {}
    for key, val in data.items():
        new_key = data_map[key]
        mapped_data[new_key] = val
    return mapped_data


if __name__ == '__main__':
    user_data = {
        "f": "Альшевский",
        "i": "Марк",
        "o": "Игоревич"
    }

    data_map = {
        "f": "surname",
        "i": "name",
        "o": "patronymic"
    }

    res = mapper(user_data, data_map)

    print(res)
