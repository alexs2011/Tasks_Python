"""
Уникализация списка
В караоке запрещено исполнять одну и ту же песню дважды за вечер.
Терминал получает список заявок и комментирует его. Напишите логику!
"""

user_input = "DRIVERS LICENSE, DON'T PLAY, AFTERGLOW, SWEET MELODY, AFTERGLOW, STREETS, AFTERGLOW, YOU BROKE ME FIRST"

# Создаём список списков: [элемент, счётчик повторов]
lst = [[x, 0] for x in user_input.split(', ')]

for track in lst:
    # Для каждого элемента находим его индекс и индексы всех его повторов (если уже не находили ранее)
    indices = [i for i, x in enumerate(lst) if x == track and x[1] == 0]
    # И увеличиваем счётчик повторов, чтобы для всех элементов со счётчиком > 0 изменить в последующем формат вывода
    for idx in indices[1:]:
        lst[idx][1] = 1

print('Список треков на сегодня:\n')

count = 1
for track in lst:
    if track[1] == 0:
        print(f'{count} {track[0]}')
        count += 1
    else:
        print(f'X {track[0]} уже пели')
