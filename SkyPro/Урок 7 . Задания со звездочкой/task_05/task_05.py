"""
https://skyengpublic.notion.site/7-926058c7c84d4c879487573427fe3dc1
Какая ты рыба
Напишите тест на рыбий характер. В тесте три вопроса, программа должна задавать их по очереди, а в конце
выдавать результат.
Результаты теста. Нужно посчитать, какой ответ встречается чаще, и вывести сообщение.
"""

import json


def load_data(filename: str) -> list[dict]:
    with open(filename, 'r', encoding='utf-8') as f_in:
        return json.load(f_in)


if __name__ == '__main__':
    filename = 'data/questions.json'
    questions = load_data(filename)

    answers = {
        "A": 0,
        "B": 0,
        "C": 0
    }

    results = {
        "A": "Вы — стайная селедка.",
        "B": "Вы — задумчивая камбала.",
        "C": "Вы — активная щука.",
        "Unknown": "Мы не смогли определить, кто вы. Будете лещом!"
    }

    for question in questions:
        print(f"\n{question['text']}\n")
        for letter, option in question['options'].items():
            print(f"{letter}. {option}")

        while True:
            user_input = input('Ваш ответ: ').upper()
            if user_input in ['A', 'B', 'C']:
                break
            print('Такого варианта ответа нет.')

        answers[user_input] += 1

    sorted_answers = list(sorted(answers.items(), key=lambda item: item[1], reverse=True))
    is_answers_equal = sorted_answers[0][1] == sorted_answers[-1][1]

    print()
    if is_answers_equal:
        print(results['Unknown'])
    else:
        print(results[sorted_answers[0][0]])
