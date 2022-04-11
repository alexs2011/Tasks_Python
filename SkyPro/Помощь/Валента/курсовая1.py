import code
import random

import bit as bit

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
    ")": "-.--.-"
}

print("Сегодня мы потренируемся расшифровывать морзянку.Нажмите Enter и начнем")

english_code = [cat, horse, run, beer]
answer = []


def print_statistics(english_code):
    """Подсчитываем правильные/неправильные ответы"""

    if answer in english_code:
        print("Отвечено верно")
    else:
        print("Отвечено неверно")

    return f"Всего задачек: 4, \n Отвечено верно: {english_code}, \n Отвечено неверно: {}"



def morse_encode(word):
    """Переводим с збуки морзе на английский"""

    word = []

    for char in word:
        word.append(morse_code[char])
    return word


def get_word():
    """Получаем случайное слово из списка"""
    english_code = [cat, horse, run, beer]
    items = random.sample(english_code, 1)
    result = ' '.join(items)

    print(result)
