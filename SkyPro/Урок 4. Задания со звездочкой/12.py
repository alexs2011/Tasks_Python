"""
Частотный список
Классическая задача на измерение частоты встречаемых слов.
Обратите внимание, слова должны считаться несмотря на регистр и знаки препинания.
"""

string = 'Если «если» перед «после», значит «после» после «если». \
Если «если» после «после», значит «после» перед «если».'

words_lst = string.lower().strip().split()

res = {}

for word in words_lst:
    tmp = ''.join([i for i in word if i.isalpha()])
    res[tmp] = res.setdefault(tmp, 0) + 1

for word, count in res.items():
    print(f'{word} - {count}')
