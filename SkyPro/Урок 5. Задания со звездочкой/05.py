"""
Секундомер
Со стандартного ввода подается количество секунд.
Выведите количество часов, минут, секунд.
Обратите внимание на формат вывода:
    - если часов 0, часы не выводятся;
    - если минут 0, минуты не выводятся.
"""


def print_time_format(sec: int) -> None:
    hours = sec // 3600
    minutes = (sec - hours * 3600) // 60
    seconds = sec - (hours * 3600 + minutes * 60)
    print(f'{str(hours) + " ч " if hours else ""}{str(minutes) + " мин " if minutes else ""}{seconds} сек')


seconds = int(input('Введите количество секунд: '))
print_time_format(seconds)
