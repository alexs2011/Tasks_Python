"""
Конвертер чисел 1
Со стандартного ввода подается число прописью, на английском языке.
Верните его в виде числа. Число максимум двузначное.
Пользователь: forty four
"""

first_digit = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
second_digit = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
anomaly_number = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

number = input('Введите число прописью: ').lower().split()

# Решение 2
match number:
    case second, first if second in second_digit and first in first_digit[1:]:
        res = (second_digit.index(second) + 1) * 10 + first_digit.index(first)
    case second, if second in second_digit:
        res = (second_digit.index(second) + 1) * 10
    case first, if first in first_digit:
        res = first_digit.index(first)
    case anomaly, if anomaly in anomaly_number:
        res = anomaly_number.index(anomaly) + 11
    case _:
        raise ValueError('Ошибка! Неверный ввод.')

# Решение 1
# if len(number) == 2:
#     if number[0] not in second_digit or number[1] not in first_digit:
#         raise ValueError('Введено не число прописью.')
#     res = (second_digit.index(number[0]) + 1) * 10 + first_digit.index(number[1])
# elif number[0] in second_digit:
#     res = (second_digit.index(number[0]) + 1) * 10
# elif number[0] in first_digit:
#     res = first_digit.index(number[0])
# elif number[0] in anomaly_number:
#     res = anomaly_number.index(number[0]) + 11
# else:
#     raise ValueError('Введено не число прописью.')

print(res)
