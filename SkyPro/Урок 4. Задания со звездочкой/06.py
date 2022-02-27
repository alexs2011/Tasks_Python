"""
Игра в города
Со стандартного ввода подается последовательность ходов при игре в “Города”. Решите, были ли нарушены правила.
[Правила игры в города](https://ru.wikipedia.org/wiki/%D0%93%D0%BE%D1%80%D0%BE%D0%B4%D0%B0_(%D0%B8%D0%B3%D1%80%D0%B0)),
если вы зумер.
Правила коротко:
    - Нельзя, чтобы один город был назван дважды
    - Следующий город начинается на ту букву, на которую закончился предыдущий
    - Если последняя буква – Ь, Ы, то на предыдущую
"""


def is_rules_correct(cities: list) -> bool:
    set_cities = set(cities)
    if len(cities) > len(set_cities):
        return False
    prev = cities[0]
    for city in cities[1:]:
        idx = -1
        if prev[-1] in ['ы', 'ь']:
            idx = -2
        if prev[idx] != city[0]:
            return False
        prev = city
    return True


message = 'Москва - Петушки'
cities = [city.strip() for city in message.lower().split('-')]

if is_rules_correct(cities):
    print('Правила не нарушены')
else:
    print('Правила нарушены')
