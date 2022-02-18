"""
В списке questions хранится 5 вопросов.
В списке answers хранится 5 ответов.
Пользователь вводит число от 1 до 5.
Программа предлагает ему ответить на вопрос. Если он ответил верно, программа сообщает об этом. Если нет – сообщает правильный ответ.
Вопросы возьмите здесь: https://www.hobobo.ru/zagadki/detskie-zagadki/
"""

questions = [
    'Тучек нет на горизонте,\nНо раскрылся в небе зонтик.\nЧерез несколько минут\nОпустился…',
    'Всегда он в работе,\nКогда говорим,\nА отдыхает,\nКогда мы молчим.',
    'По лужку он важно бродит,\nИз воды сухим выходит,\nНосит красные ботинки,\nДарит мягкие перинки.',
    'В Москве говорят, а у нас слышно.',
    'Плотник острым долотом\nСтроит дом с одним окном.'
]

answers = ['Парашют', 'Язык', 'Гусь', 'Радио', 'Дятел']

try:
    number = int(input('Введите число от 1 до 5: '))
except ValueError as e:
    print('Ошибка. Введено не число!')
    quit()

if 1 <= number <= 5:
    print(f'\nОтветьте на вопрос №{number}:\n')
    print(questions[number - 1])
    answer = input('\nВаш ответ: ').lower().capitalize()
    if answer == answers[number - 1]:
        print('Ответ верен!')
    else:
        print('Ответ неверен!')
        print(f'Правильный ответ: {answers[number - 1]}')
else:
    print('Ошибка. Введено число вне диапазона 1-5!')
