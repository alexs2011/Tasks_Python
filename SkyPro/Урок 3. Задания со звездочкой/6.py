"""
Гласные и согласные
Со стандартного ввода подается буква.
Определите, гласная она, согласная, цифра или знак препинания.
"""

import string

lower_vowels = 'аеёиоуыэюя' + 'aeiou'
lower_consonants = 'бвгджзйклмнпрстфхцчшщъь' + 'bcdfghjklmnpqrstvwxyz'
digits = string.digits
punctuation_marks = string.punctuation + '—«»'

ch = input('Введите символ: ')
if len(ch) != 1:
    raise ValueError('Введён не 1 символ!')

if ch in punctuation_marks:
    print('Это знак препинания')
elif ch in digits:
    print('Это цифра')
elif ch in lower_vowels:
    print('Это маленькая гласная')
elif ch in lower_consonants:
    print('Это маленькая согласная')
elif ch.lower() in lower_vowels:
    print('Это большая гласная')
elif ch.lower() in lower_consonants:
    print('Это большая согласная')
else:
    print('Это непонятно что')
