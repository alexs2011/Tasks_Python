import utils
from pprint import pprint as pp

questions = utils.load_questions()
stats = {"points": 0, "correct": 0, "incorrect": 0}
questions_total = utils.count_questions(questions)
questions_used = 0

while questions_used < questions_total:

    utils.show_field(questions)
    print("Выберите вопрос")
    user_input = input()

    if user_input == "стоп":
        break

    questions_current = utils.parse_input(user_input, questions)

    if questions_current == False:
        print("Нет, такого вопроса нет!")
        continue

    cat = questions_current.get("cat")
    price = questions_current.get("price")
    question = questions_current.get("question")
    answer = questions_current.get("answer")

    utils.show_question(question)

    user_input = input()

    if user_input == answer:
        print("Ответ верны")
        stats["points"] += int(price)
        stats["correct"] += 1
    else:
        print("Ответ неверны")
        stats["points"] -= int(price)
        stats["incorrect"] += 1

    questions[cat][price]['asked'] = True
    questions_used += 1
    print()

utils.show_stats(stats)
utils.save_results_to_file(stats)
