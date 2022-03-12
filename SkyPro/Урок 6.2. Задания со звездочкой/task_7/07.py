"""
Знаки
В папке расположено несколько текстовых файлов. Со стандартного ввода подается название текстового файла.
Необходимо открыть файл, посчитать в нем количество слов, символов, предложений (предложение — это точка, пробел и
большая буква после пробела), вывести в формате:
    Предложений - X
    Слов - X
    Символов – X
"""

filename = input('Введите название файла: ')

with open(filename, 'r', encoding='utf-8') as f_in:
    text = f_in.read()

words = text.split()

sentence_count = 1 if text else 0

for i, word in enumerate(words):
    if word[-1] == '.' and i < len(words) - 1 and words[i + 1][0].isupper():
        sentence_count += 1

print(f'Предложений - {sentence_count}')
print(f'Слов - {len(words)}')
print(f'Символов - {len(text)}')
