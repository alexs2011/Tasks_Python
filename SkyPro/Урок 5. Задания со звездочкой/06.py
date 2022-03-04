"""
Сумма мелочью.
Дать сдачу — простая задача, если все монеты и купюры есть в наличии, но как быть, если часть номинала закончилась?
В функцию первым аргументом подается сумма в рублях.
Вторым аргументом подается список доступных номиналов монет.
Например:
    Сумма
    27
    Доступные номиналы
    10, 5, 2, 1
Функция должна возвращать словарь, в котором указано количество каждого номинала.
"""


def change(amount: int, coins_value: list[int]) -> dict:
    d = dict.fromkeys(coins_value, 0)
    sorted_coins_value = sorted(coins_value, reverse=True)
    tmp_sum = 0
    for value in sorted_coins_value:
        d[value] = (amount - tmp_sum) // value
        tmp_sum += d[value] * value
    return d


summa = int(input('Введите сумму: '))
coins = list(map(int, input('Введите номиналы: ').split()))

print(change(summa, coins))
