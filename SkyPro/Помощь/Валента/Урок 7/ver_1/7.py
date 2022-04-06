import utils

from pprint import pprint as pp


questions = utils.load_questions()
stats = {"points": 0, "correct": 0, "incorrect": 0}


while True:

    utils.show_field(questions)
    print("Выберите вопрос")
    user_input = input()

    questions_current = utils.parse_input(user_input, questions)

    utils.show_question(questions)

    user_input = input()

    if user_input == answer:
        print("Ответ верны")
        stats["points"] +=int(price)
        stats["points"] += 1
    else:
        print("Ответ неверны")
        stats["points"] -= int(price)
        stats["incorrect"] += 1

    questions[cat][price]['asked'] = True

    print()

utils.show_stats(stats)
utils.save_results_to_file(stats)

