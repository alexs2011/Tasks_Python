"""
Почти Excel
Создайте Google Документ или документ в Excel, добавьте туда колонку с числами.
Сохраните в `expenses.csv` и сложите числа во второй колонке.
"""

import csv

prices = []

with open('expenses.csv', 'r', encoding='utf-8') as f_in:
    reader = csv.reader(f_in)
    for row in reader:
        prices.append(int(row[1]))

print(f'Всего позиций: {len(prices)}')
print(f'Сумма: {sum(prices)}')
