"""
Библиотека валидаторов (строки, библиотеки)
Создайте файл validators.py, в нем создайте функции:
1. Проверки пин-кода check_pin(pin) – проверяет, является ли строка четырехбуквенным пин-кодом.
Пин-код не может содержать 4 одинаковые цифры и быть равен 1234.
2. Проверки пароля check_pass – проверяет, чтобы пароль был не меньше 8 символов, содержал буквы и цифры.
3. Проверки почты check_mail – проверяет наличие собачки и точки.
4. Проверки имени check_name – проверяет содержание в имени только **русских** букв и пробелов.
Каждая из функций валидаторов возвращает True или False.
Создайте файл task_4.py и в нем импортируйте функции-валидаторы.
С их помощью проверьте несколько наборов значений.
"""

import validators

d = {
    0: {
        'pin': '1239',
        'pass': 'secretd00r',
        'mail': 'local@skypro',
        'name': 'Данил',
    },
    1: {
        'pin': '3333',
        'pass': 'huskyeye5',
        'mail': 'you(at)sky.pro',
        'name': 'Р_и_т_а',
    },
    2: {
        'pin': '1234',
        'pass': 'secret',
        'mail': 'me@sky.pro',
        'name': 'К0нстантин',
    },
    3: {
        'pin': '00011',
        'pass': 'm3wm3wm3w',
        'mail': '@lizaveta',
        'name': 'А Ф',
    },
    4: {
        'pin': '8765',
        'pass': 'fh43j_!',
        'mail': 'alarm@gmail.com',
        'name': 'Елена',
    },
}

for value in d.values():
    is_correct = True

    print('\nПроверка набора данных: ')
    print(f'Пин-код: {value["pin"]}, пароль: {value["pass"]}, почта: {value["mail"]}, имя: {value["name"]}')

    if not validators.check_pin(value['pin']):
        print("Неверный пин")
        is_correct = False
    if not validators.check_pass(value['pass']):
        print("Неверный пароль")
        is_correct = False
    if not validators.check_mail(value['mail']):
        print("Неверная почта")
        is_correct = False
    if not validators.check_name(value['name']):
        print("Неверное имя")
        is_correct = False
    if is_correct:
        print("Набор данных верен")
