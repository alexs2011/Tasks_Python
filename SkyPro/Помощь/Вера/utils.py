import json
from pprint import pprint as pp


def load_questions():
    """загргужаем словарь с вопросами"""
    with open("questions.json", "r", encoding="utf-8") as file:
        questions = json.load(file)
    return questions


def count_questions(questions):
    """Получает общее количество вопросов"""
    counter = 0
    for cat_questions in questions.values():
        for question in cat_questions:
            counter += 1
    return counter


def show_field(questions):
    """Распечатывает игровое поле"""
    top_level_cats = questions.keys()

    for top_cat in top_level_cats:
        print(top_cat.ljust(13), end="")
        cat_questions = questions[top_cat]
        for question_price, question_data in cat_questions.items():
            if question_data["asked"] == True:
                print(" " * 4, end=" ")
            else:
                print(str(question_price).ljust(4), end=" ")
        print()


def parse_input(user_input, questions):
    user_input_parsed = user_input.split(" ")

    """Если не 2 сегмента в пользовательском вводе - значит ошибка"""
    if len(user_input_parsed) != 2:
        return False

    """Вытаскиваем из пользовательского ввода категорию и цену"""
    cat = user_input_parsed[0].title()
    price = user_input_parsed[1]

    """Если указанной категории нет, то ошибка"""
    if cat not in questions:
        return False

    category_from_questions = questions[cat]

    """Если указанной цены нет - то ошибка"""
    if price not in category_from_questions:
        return False

    question_data = category_from_questions[price]

    """Если вопроос уже задан - то ошибка"""
    if question_data["asked"]:
        return False

    question_text = question_data['question']
    question_answer = question_data['answer']

    return {"cat": cat, "price": price, "question": question_text, "answer": question_answer}


def show_question(question_text):
    """Распечатываем вопрос"""
    print(f"Слово {question_text} в переводе означает ... ")


def show_stats(stats):
    """Выводит статистику"""
    print("У нас закончились вопросы!")
    print("")
    print(f"Ваш счет:         {stats.get('points')}")
    print(f"Верных ответов:   {stats.get('correct')}")
    print(f"Неверных ответов: {stats.get('incorrect')}")


def save_results_to_file(stats):
    filename = "record.json"
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(stats, file, ensure_ascii=False)

