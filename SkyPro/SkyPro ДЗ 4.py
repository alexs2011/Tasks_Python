words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}

words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
}

words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
}

levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично",
}

answers = {}

difficulty_levels = (('легкий', 'words_easy'), ('средний', 'words_medium'), ('сложный', 'words_hard'))

str_levels = tuple(x[0] for x in difficulty_levels)

while True:
    print('Выберите уровень сложности.')
    print(', '.join(str_levels).capitalize())
    user_input = input().lower()
    if user_input in str_levels:
        idx = str_levels.index(user_input)
        words = eval(difficulty_levels[idx][1])
        print(f'Выбран уровень сложности, мы предложим {len(words)} слов, подберите перевод.\n')
        break
    else:
        print('Введённый уровнь сложности не найден.\nПопробуйте ещё раз.\n')

for word, translation in words.items():
    print(f'{word}, {len(word)} букв, начинается на {translation[0]}...')
    user_input = input().lower()
    answers[word] = user_input == translation
    print(f'{"Верно." if answers[word] else "Неверно."} {word.capitalize()} — это {translation}\n')

res_lst = [[], []]  # False, True
for key, val in answers.items():
    res_lst[int(val)].append(key)

for i in range(1, -1, -1):
    print(f"{'Правильно' if i == 1 else 'Неправильно'} отвечены слова:")
    print('\n'.join(res_lst[i]) + '\n')

print('Ваш ранг:')
print(levels[len(res_lst[1])])
