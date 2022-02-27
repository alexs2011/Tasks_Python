"""
Почта на корпоративном домене
Со стандартного ввода подается почта.
Есть список бесплатных почт в списке. Нужно проверить, является ли почта почтой и не расположена ли
она на бесплатном домене.
Бесплатные домены почты:
yandex.ru, mail.ru, gmail.com , yahoo.com, rambler.ru
"""

email_free_lst = ['yandex.ru', 'mail.ru', 'gmail.com', 'yahoo.com', 'rambler.ru']

user_input = input('Введите почту: ')

splitted_email = list(filter(None, user_input.split('@')))
if len(splitted_email) != 2:
    print('Это вообще не почта')
    quit()

if splitted_email[1] in email_free_lst:
    print('Это почта, она на бесплатном домене')
else:
    print('Это почта, она на корпоративном домене')
