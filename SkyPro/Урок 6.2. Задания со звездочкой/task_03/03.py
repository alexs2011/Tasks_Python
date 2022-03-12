"""
Хороший список, плохой список, злой список
1. С помощью Google Spreadsheets создайте таблицу, в первой колонке которой будут имена студентов,
а во второй — их баллы за экзамены.
2. Сохраните данные в файл csv.
3. Прочитайте данные из файла, рассортируйте студентов по двум файлам passed.txt и failed в реальном времени
(с помощью построчного добавления в файл). Проходной балл равен 75.
"""

import csv
import os


def write_exams_result(name: str, is_passed: bool) -> None:
    filename = 'passed.txt' if is_passed else 'failed.txt'
    with open(filename, 'a', encoding='utf-8') as f_out:
        if os.stat(filename).st_size == 0:  # если файл пуст
            f_out.write(name)
        else:
            f_out.write(f'\n{name}')


students_results = []

with open('score.csv', encoding='utf-8') as f_in:
    reader = csv.reader(f_in)
    for row in reader:
        students_results.append([row[0], int(row[1])])

for student, res in students_results:
    write_exams_result(student, res >= 75)
