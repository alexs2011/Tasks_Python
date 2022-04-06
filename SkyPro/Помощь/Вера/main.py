import utils
from pprint import pprint as pp

questions = utils.load_questions()
stats = {"point": 0, "correct": 0, "incorrect": 0}
questions_total = utils.count_questions(questions)
questions_used = 0

while questions_used < questions_total:

    utils.show_field(questions)
    print("Выберите вопрос")
    user_input = input()

    if user_input == "стоп":
        break

    question_current = utils.parse_input(user_input, questions)
    if question_current == False:
        print("Нет, такого вопроса нет!")
        continue

    cat = question_current.get("cat")
    price = question_current.get("price")
    question = question_current.get("question")
    answer = question_current.get("answer")

    utils.show_question(question)

    user_input = input()

    if user_input == answer:
        print("Ответ верный")
        stats["points"] += int(price)
        stats["correct"] += 1
    else:
        print("Ответ неверный")
        stats["points"] -= int(price)
        stats["incorrect"] += 1
    questions[cat][price]['asked'] = True
    questions_used += 1
    print()

utils.show_stats(stats)
utils.save_results_to_file(stats)