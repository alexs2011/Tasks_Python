"""
Тестирование из файла
Создайте файл в формате csv, где:
    - в первой колонке будет номер вопроса,
    - во второй — вопрос,
    - в третьей — первый вариант ответа,
    - в четвертой — второй вариант,
    - в пятой — верный ответ.

Вопросы возьмите здесь: [https://www.usingenglish.com/quizzes/29.html](https://www.usingenglish.com/quizzes/29.html)
Реализуйте тест с вопросами из документа.
"""

import csv

right_answers_count = 0

with open('tests.csv', 'r', encoding='utf-8') as f_in:
    reader = csv.reader(f_in)
    for i, question, answ_1, answ_2, right_answ in reader:
        print(f'\nQuestion {i}. {question}')
        print(answ_1)
        print(answ_2)
        user_input = input('Your answer: ').lower()
        if user_input == right_answ:
            print('Верно!')
            right_answers_count += 1
        else:
            print(f'Нет. Верный ответ – {right_answ}')

print('\nТест завершён.')
print(f'Верные ответы {right_answers_count}/{i}')
