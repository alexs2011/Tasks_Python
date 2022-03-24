import random

import utils

if __name__ == '__main__':

    questions = utils.load_questions()

    is_mode_random = False

    user_input = input("Задавать ли вопросы в случайном порядке (y/n): ").lower()
    if user_input == 'y':
        is_mode_random = True
        available_questions_idx = list(range(len(questions)))

    for i in range(len(questions)):
        cur_question_idx = i
        if is_mode_random:
            cur_question_idx = random.choice(available_questions_idx)
            available_questions_idx.remove(cur_question_idx)

        question = questions[cur_question_idx]

        print(f"\n{question.build_question()}")

        user_input = input("Ответ: ").lower()
        utils.update_statistics(question, user_input)

        print(question.build_feedback())

    print("\nВот и всё!")
    print(utils.build_statistics(questions))
