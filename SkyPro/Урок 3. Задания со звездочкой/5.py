"""
Конвертер чисел 2
Со стандартного ввода **цифрами** подается положительное число
Верните его **прописью**. Число максимум двузначное.
"""

first_digit = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
second_digit = ['десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят',
                'девяносто']
anomaly_number = ['одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать',
                  'восемнадцать', 'девятнадцать']

try:
    number = int(input('Введите число: '))
    if not 0 <= number <= 99:
        raise ValueError("Число должно быть в диапазоне от 0 до 99.")
except ValueError as e:
    print(f'Ошибка: {e}')
    quit()

res = None
if not 11 <= number <= 19:
    first = number % 10
    second = number // 10
    if second == 0:
        res = first_digit[first]
    elif first == 0:
        res = second_digit[second - 1]
    else:
        res = f'{second_digit[second - 1]} {first_digit[first]}'
else:
    first = number % 10
    res = anomaly_number[first - 1]

print(res)
