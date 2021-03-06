"""
Замечательные соседи
В словаре хранится список элементов, где ключ – номер элемента, а значение – название на русском языке.
Ключи – это числа.
    28: Никель
    29: Медь
    30: Цинк
На вход подается номер, на выходе должны быть соседи этого элемента. Элементы взяты из таблицы Менделеева.
"""

d = {
    1: "Водород",
    2: "Гелий",
    3: "Литий",
    4: "Бериллий",
    5: "Бор",
    6: "Углерод",
    7: "Азот",
    8: "Кислород",
    9: "Фтор",
    10: "Неон",
}

user_input = int(input('Введите номер элемента: '))

if not 1 <= user_input <= len(d):
    print('Элемент не найден')
    quit()

prev = user_input - 1
next = user_input + 1

print(f'{user_input} - это {d[user_input]}')
print('Соседи:')

if prev > 0:
    print(f'{prev} - это {d[prev]}')
if next <= len(d):
    print(f'{next} - это {d[next]}')
