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
