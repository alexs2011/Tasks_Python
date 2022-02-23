import random

morse_code = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-",
    " ": "/",
}

words = ['code', 'bit', 'list', 'soul', 'next', 'well played']

# Список результатов, индексы в котором соответствуют индексам элементов в списке words.
# Это необходимо для того, чтобы при выборе случайных элементов из words они не повторялись.
answers = [None] * len(words)


def morse_encode(word):
    """
    Конвертирует символы строки word в символы азбуки Морзе.
    """
    code_lst = [morse_code[ch] for ch in word]
    return ' '.join(code_lst)


def get_word():
    """
    Находит и возвращает уникальное случайное слово из списка words.
    """
    # Находим индексы тех слов, которые ещё не были заданы
    free_indices = [i for i, x in enumerate(answers) if x is None]
    # И выбираем из них случайный, тем самым получая возможность взять случайное,
    # но при этом уникальное слово из words.
    idx = random.choice(free_indices)
    return words[idx]


def print_statistics(answers):
    """
    Вычисляет общее количество вопросов, количество правильных и неправильных ответов и выводит статистику.
    """
    right_answers_count = len([x for x in answers if x])
    print(f'Всего задачек: {len(answers)}')
    print(f'Отвечено верно: {right_answers_count}')
    print(f'Отвечено неверно: {len(answers) - right_answers_count}')


_ = input('Сегодня мы потренируемся расшифровывать азбуку Морзе.\nНажмите Enter и начнём: ')

for i in range(len(words)):
    # Получаем случайное слово из списка и преобразовываем в последовательность азбуки Морзе.
    word = get_word()
    word_encode = morse_encode(word)
    # Находим индекс этого слова, чтобы в последующем изменить соответствующий ему элемент в списке ответов.
    idx = words.index(word)

    print(f'Слово {i + 1} - {word_encode} {word}')
    user_input = input('Введите расшифровку: ')

    if user_input[1:].islower() and user_input.lower() == word:
        print(f'Верно, {word.capitalize()}!\n')
        answers[idx] = True
    else:
        print(f'Неверно, {word.capitalize()}!\n')
        answers[idx] = False

print_statistics(answers)
