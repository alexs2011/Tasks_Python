"""
Урбанистический рейтинг
Топы городов могут быть составлены не только по численности, площади и самым высоким небоскребам.
Вот несколько милейших рейтингов (они ненастоящие, мы их сами придумали).
Пользователь вводит название города, приложение возвращает среднюю позицию в списках
(среднее арифметическое между всеми позициями).
"""

# по количеству скамеечек на человека
top_by_benches = ['Auckland', 'Osaka', 'Adelaide', 'Geneva', 'Melbourne']

# по количеству фонтанчиков на человека
top_by_fountains = ['Adelaide', 'Geneva', 'Osaka', 'Melbourne', 'Auckland']

# по количеству качелек на человека
top_by_swings = ['Osaka', 'Adelaide', 'Geneva', 'Melbourne', 'Auckland']

town = input('Введите название города: ')

if town not in top_by_benches:
    print('Такого города нет в рейтингах.')
    quit()

ratings = [top_by_benches.index(town) + 1,
           top_by_fountains.index(town) + 1,
           top_by_swings.index(town) + 1]

print(f'\nПо количеству скамеечек: №{ratings[0]}')
print(f'По количеству фонтанчиков: №{ratings[1]}')
print(f'По количеству качелек: №{ratings[2]}')
print(f'В среднем занимает позицию: {sum(ratings) / len(ratings):.0f}')
