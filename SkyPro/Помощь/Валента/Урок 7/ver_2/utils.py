import json
from pprint import pprint as pp


def load_questions():
    with open("questions.json", "r", encoding="utf-8") as file:
        questions = json.load(file)
    return questions


def count_questions(questions):
    counter = 0

    for cat_questions in questions.values():
        counter += len(cat_questions)

    return counter


def show_field(questions):
    top_level_cats = questions.keys()

    for top_cat in top_level_cats:
        print(top_cat.ljust(13), end="")
        cat_questions = questions[top_cat]
        for questions_price, questions_data in cat_questions.items():
            if questions_data["asked"] == True:
                print(" " * 4, end=" ")
            else:
                print(str(questions_price).ljust(4), end=" ")
        print()


def parse_input(user_input, questions):
    user_input_parsed = user_input.split(" ")

    if len(user_input_parsed) != 2:
        return False

    cat = user_input_parsed[0].title()
    price = user_input_parsed[1]

    if cat not in questions:
        return False

    category_from_questions = questions[cat]

    if price not in category_from_questions:
        return False

    question_data = category_from_questions[price]

    if question_data["asked"]:
        return False

    question_text = question_data["question"]
    question_answer = question_data["answer"]

    return {"cat": cat, "price": price, "question": question_text, "answer": question_answer}


def show_question(question_text):
    print(f"Слово {question_text} в переводе означает ...")


def show_stats(stats):
    print("У нас закончились вопросы")
    print("")
    print(f"Ваш счет:       {stats.get('points')}")
    print(f"Верных ответов: {stats.get('correct')}")
    print(f"Неверных ответов: {stats.get('incorrect')}")


def save_results_to_file(stats):
    filename = "record.json"
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(stats, file, ensure_ascii=False)



