"""
Число 145 интересно тем, что 1! + 4! + 5! = 145.
Задача: в диапазоне до 1 млн. или более найти ещё подобные числа — сумма
факториалов цифр которых равна самому числу.
"""

import math
import time


def sum_factorials_of_digits(number):
    s = 0
    while number:
        s += factorials[number % 10]
        number //= 10
    return s


factorials = []
res = []
n = 10_000_000

for i in range(0, 10):
    factorials.append(math.factorial(i))

t_beg = time.time()
cached_sum = 0
for number in range(n):
    last_digit = number % 10
    if last_digit == 0:
        cached_sum = sum_factorials_of_digits(number // 10)
        s = cached_sum + factorials[0]
    else:
        s = cached_sum + factorials[last_digit]
    if s == number:
        res.append(number)
t_end = time.time()
print(t_end - t_beg)
print(res)
