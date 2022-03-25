import random

import utils

if __name__ == '__main__':

    questions = utils.load_questions()

    user_input = input("Задавать ли вопросы в случайном порядке (y/n): ").lower()
    if user_input == 'y':
        random.shuffle(questions)

    for question in questions:

        print(f"\n{question.build_question()}")

        user_input = input("Ответ: ").lower()
        utils.update_statistics(question, user_input)

        print(question.build_feedback())

    print("\nВот и всё!")
    print(utils.build_statistics(questions))
