import json
import os


def load_questions(filename: str = 'data/questions.json') -> dict:
    """
    Загружает вопросы из файла формата json и возвращает словарь
    """
    with open(filename, 'r', encoding='utf-8') as f_in:
        return json.load(f_in)


def show_field(game_field: dict) -> None:
    """
    Вывод на экран игрового поля
    """
    topics = []
    for topic in game_field.keys():
        topics.append(topic)

    max_topic_length = len(max(topics))
    placeholder = ' ' * 3

    for topic, topic_questions in game_field.items():
        print(topic.ljust(max_topic_length), end=' ')
        for score, question in topic_questions.items():
            print(score if not question['asked'] else placeholder, end=placeholder)
        print()


def parse_input(string: str, game_field: dict) -> bool | list[str]:
    """
    Проверка введённых пользователем данных на соответствие формату и наличие вопроса такой категории и стоимости на
    игровом поле
    """
    data = string.lower().capitalize().strip().split()
    # проверяем, что введено 2 значения
    if len(data) != 2:
        return False
    # проверяем, что введённая категория есть в перечне категорий
    if data[0] not in game_field.keys():
        return False
    # проверяем, что введённая стоимость вопроса существует
    if data[1] not in game_field[data[0]].keys():
        return False
    # проверяем, что такой вопрос ещё не задавали
    if game_field[data[0]][data[1]]['asked']:
        return False
    return data


def show_question(game_field: dict, q: list, statistics: dict) -> None:
    """
    Показывает вопрос по заданной категории и стоимости, проверяет правильность введённого ответа и подсчитывает
    статистику
    """
    cur_question = game_field[q[0]][q[1]]
    user_answer = input(f'Слово {cur_question["question"]} в переводе означает ...\n').lower()
    cur_question['asked'] = True
    if user_answer == cur_question['answer']:
        statistics['points'] += int(q[1])
        statistics['correct'] += 1
        print(f"Верно, +{q[1]} очков. Ваш счет: {statistics['points']}\n")
    else:
        statistics['points'] -= int(q[1])
        statistics['incorrect'] += 1
        print(f"Неверно, на самом деле: {cur_question['answer'].capitalize()}. -{q[1]} очков. "
              f"Ваш счет: {statistics['points']}\n")


def show_stats(statistics: dict) -> None:
    """
    Показывает результаты после окончания игры
    """
    print('У нас закончились вопросы!\n')
    print(f'Ваш счет: {statistics["points"]}')
    print(f'Верных ответов: {statistics["correct"]}')
    print(f'Неверных ответов: {statistics["incorrect"]}')


def save_results_to_file(statistics: dict, filename: str = 'data/results.json') -> None:
    """
    Сохраняет результат игры в файл с общим списком результатов в формате json
    """
    with open(filename, 'r', encoding='utf-8') as f_in:
        if os.stat(filename).st_size == 0:  # если файл пуст
            total_stat = [statistics]
        else:
            total_stat = json.load(f_in)
            total_stat.append(statistics)

    with open(filename, 'w', encoding='utf-8') as f_out:
        json.dump(total_stat, f_out)


if __name__ == '__main__':
    cur_stat = {
        'points': 0,
        'correct': 0,
        'incorrect': 0
    }

    questions = load_questions()

    number_of_questions = 0
    for val in questions.values():
        number_of_questions += len(val.keys())

    for _ in range(number_of_questions):
        show_field(questions)
        while True:
            user_input = input('\nВведите вопрос и стоимость: ')
            parsing_res = parse_input(user_input, questions)
            if parsing_res:
                break
            print('Такого вопроса нет, попробуйте еще раз!')
        show_question(questions, parsing_res, cur_stat)

    show_stats(cur_stat)
    save_results_to_file(cur_stat)
