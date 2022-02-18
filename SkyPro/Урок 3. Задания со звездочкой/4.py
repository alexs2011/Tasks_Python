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

res = None
if len(number) == 2:
    if number[0] not in second_digit or number[1] not in first_digit:
        raise ValueError('Введено не число прописью.')
    res = (second_digit.index(number[0]) + 1) * 10 + first_digit.index(number[1])
elif number[0] in second_digit:
    res = (second_digit.index(number[0]) + 1) * 10
elif number[0] in first_digit:
    res = first_digit.index(number[0])
elif number[0] in anomaly_number:  # значит число от 11 до 19
    res = anomaly_number.index(number[0]) + 11
else:
    raise ValueError('Введено не число прописью.')

print(res)
