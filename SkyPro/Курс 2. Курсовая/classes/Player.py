class Player:
    def __init__(self, player_name: str) -> None:
        self.name = player_name

        self.used_subwords = []

    def __repr__(self):
        return f"Name: {self.name}\nUsed subwords: {self.used_subwords}"

    def __len__(self) -> int:
        """
        Подсчитывает количество использованных подслов.
        """
        return len(self.used_subwords)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, player_name: str) -> None:
        self.validate_name(player_name)
        self.__name = player_name

    @staticmethod
    def validate_name(player_name: str) -> None:
        """
        Проверяет, что имя не пусто, либо не содержит только пробельные символы.
        """
        if not player_name.strip():
            raise ValueError("Имя не должно быть пустым!")

    def add(self, subword) -> None:
        """
        Добавляет слово в список использованных слов.
        """
        self.used_subwords.append(subword)

    def is_subword_used(self, subword: str) -> bool:
        """
        Проверяет, было ли использовано подслово раньше.
        """
        return subword in self.used_subwords
