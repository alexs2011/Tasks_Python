import json
import Question


def load_questions(filename: str = 'data/questions.json') -> list[Question]:
    """
    Загрузка данных из файла json и сохранение их в список объектов типа Question.
    """
    with open(filename, 'r', encoding='utf-8') as f_in:
        raw_questions = json.load(f_in)
    return [Question.Question(x['q'], int(x['d']), x['a']) for x in raw_questions]


def update_statistics(question: Question, answer: str) -> None:
    """
    Запись ответа пользователя и изменение флага того, задан ли вопрос.
    """
    question.user_answer = answer
    question.is_asked = True


def build_statistics(q: list[Question]) -> str:
    """
    Возвращает статистику по игре в удобном для пользователя виде.
    """
    stats = {
        "right_answers": 0,
        "total_answers": 0,
        "score": 0
    }

    for question in q:
        stats['total_answers'] += 1
        if question.is_correct():
            stats['right_answers'] += 1
            stats['score'] += question.score

    return f"Отвечено {stats['right_answers']} вопроса из {stats['total_answers']}\nНабрано баллов: {stats['score']}"
