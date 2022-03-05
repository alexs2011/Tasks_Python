"""
Фильтрация списка словарей
Напишите функцию проверки пользователей для отбора кандидатов в космическую экспедицию Mars Two. Функция должна
возвращать True, если рост пользователя от 157 до 175 и вес от 50 до 70 кг.
Напишите функцию, которая принимает список словарей и фильтрует его, возвращая только подходящих кандидатов,
и использует функцию validate.
"""

candidates = [
    {'name': 'Юрий', 'h': 157, 'w': 60},
    {'name': 'Олег', 'h': 177, 'w': 65},
    {'name': 'Юлия', 'h': 165, 'w': 57},
    {'name': 'Аркадий', 'h': 174, 'w': 59},
]


def validate(data: dict) -> bool:
    if 157 <= data['h'] <= 175 and 50 <= data['w'] <= 70:
        return True
    return False


def validate_list(candidates: list[dict]) -> list[dict]:
    return [x for x in candidates if validate(x)]


assert validate({'h': 160, 'w': 60}), 'Ошибка для роста 160 и веса 60'
assert validate({'h': 180, 'w': 60}) is False, 'Ошибка для роста 180 и веса 60'
assert validate({'h': 164, 'w': 75}) is False, 'Ошибка для роста 164 и веса 75'
assert validate({'h': 180, 'w': 80}) is False, 'Ошибка для роста 180 и веса 80'

assert validate_list(candidates) == [candidates[0], candidates[2], candidates[3]], 'Ошибка - неверный список кандидатов'
