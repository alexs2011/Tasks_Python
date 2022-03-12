"""
Документ с определениями
С помощью Google Spreadsheets создайте таблицу, в первой колонке которой будут термины, а во второй — определения.
Скачайте файл в формате csv (Файл > Скачать > CSV).
Напишите программу, которая считывает термин определения в словарь.
Примите со стандартного ввода запрос пользователя и, если это известный термин, верните определение.
Если нет — выведите список известных терминов. Пользователь может ввести название файла в любом регистре.
"""

import csv

d = {}

with open('definitions.csv', encoding='utf-8') as f_in:
    reader = csv.reader(f_in)
    for row in reader:
        d[row[0].lower()] = row[1]

user_input = input('Введите термин: ').lower()

if user_input in d.keys():
    print(f"{user_input.capitalize()} - {''.join(d[user_input][0].lower() + d[user_input][1:])}")
else:
    print('По вашему запросу ничего не найдено, могу предложить:')
    for key in d.keys():
        print(f'- {key.capitalize()}')
