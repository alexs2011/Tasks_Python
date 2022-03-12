"""
Оценки за выступления
Создайте csv-файл с оценками на выставке змей.
В первой колонке — имя змеи, в следующих — оценки:
    - за технику,
    - внешний вид,
    - шипение.
Посчитайте среднее арифметическое по каждой колонке и выведите его.
"""

import csv

d = {}

with open('score.csv', 'r', encoding='utf-8') as f_in:
    reader = csv.reader(f_in)
    for row in reader:
        d[row[0]] = sum(map(int, row[1:])) / 3

for name, val in d.items():
    print(f'{name}: {val:.1f}')
