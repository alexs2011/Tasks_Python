"""
Конвертер
Создайте файл miles.txt со следующим содержимым:
    145.0
    2100.0
    17.5
    0.75
    4223.0
Создайте пустой файл kilometers.txt.
Напишите программу, которая считает числа из первого файла, переводит из миль в километры и сохраняет во втором файле.
"""

coef = 1.60934

with open('miles.txt', 'r', encoding='utf-8') as f_in:
    miles_lst = [float(x) for x in f_in]

km_lst = [x * coef for x in miles_lst]

with open('kilometers.txt', 'w', encoding='utf-8') as f_out:
    f_out.writelines('\n'.join(map(str, km_lst)))
