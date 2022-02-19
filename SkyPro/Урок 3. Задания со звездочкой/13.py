"""
Уникализация списка
В караоке запрещено исполнять одну и ту же песню дважды за вечер.
Терминал получает список заявок и комментирует его. Напишите логику!
"""

user_input = "DRIVERS LICENSE, DON'T PLAY, AFTERGLOW, SWEET MELODY, AFTERGLOW, STREETS, AFTERGLOW, YOU BROKE ME FIRST"

lst = [[x, 0] for x in user_input.split(', ')]

for track in lst:
    indices = [i for i, x in enumerate(lst) if x == track and x[1] == 0]
    for i, idx in enumerate(indices):
        lst[idx][1] = i

print('Список треков на сегодня:\n')

count = 1
for track in lst:
    if track[1] == 0:
        print(f'{count} {track[0]}')
        count += 1
    else:
        print(f'X {track[0]} уже пели')
