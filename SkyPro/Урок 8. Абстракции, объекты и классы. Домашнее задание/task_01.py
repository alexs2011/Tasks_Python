import json
import random


class Question:
    MAX_DIFFICULTY = 5
    POINTS_PER_EVERY_DIFFICULTY_LEVEL = 10

    def __init__(self, question: str, difficulty: int, right_answer: str) -> None:
        self.question = question
        self.difficulty = difficulty
        self.right_answer = right_answer

        self.is_asked = False
        self.user_answer = None
        self.score = difficulty * self.POINTS_PER_EVERY_DIFFICULTY_LEVEL

    def __repr__(self) -> str:
        return f"\
        \nВопрос: {self.question}\
        \nСложность: {self.difficulty}/{self.MAX_DIFFICULTY}\
        \nВерный ответ: {self.right_answer}\
        \nЗадан ли вопрос: {self.is_asked}\
        \nОтвет пользователя: {self.user_answer}\
        \nБаллы за вопрос: {self.score}"

    def get_points(self) -> int:
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        return self.score

    def is_correct(self) -> bool:
        """Возвращает True, если ответ пользователя совпадает
        с верным ответом иначе False.
        """
        return self.right_answer == self.user_answer

    def build_question(self) -> str:
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        return f"Вопрос: {self.question}\nСложность: {self.difficulty}/{self.MAX_DIFFICULTY}"

    def build_feedback(self) -> str:
        """Возвращает:
        Ответ верный, получено __ баллов
        Ответ неверный, верный ответ __
        """
        if self.is_correct():
            return f"Ответ верный, получено {self.score} баллов"
        return f"Ответ неверный, верный ответ: {self.right_answer}"


def load_questions(filename: str = 'data/questions.json') -> list[Question]:
    """
    Загрузка данных из файла json и сохранение их в список объектов типа Question.
    """
    with open(filename, 'r', encoding='utf-8') as f_in:
        raw_questions = json.load(f_in)
    return [Question(x['q'], int(x['d']), x['a']) for x in raw_questions]


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


if __name__ == '__main__':

    questions = load_questions()

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
        update_statistics(question, user_input)

        print(question.build_feedback())

    print("\nВот и всё!")
    print(build_statistics(questions))
