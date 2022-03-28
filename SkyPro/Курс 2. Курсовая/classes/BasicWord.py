class BasicWord:
    def __init__(self, word: str, subwords: list[str]) -> None:
        self.word = word
        self.subwords = subwords

    def __repr__(self):
        return f"Word: {self.word}\nSubwords: {self.subwords}"

    def __len__(self) -> int:
        """
        Подсчитывает количество подслов.
        """
        return len(self.subwords)

    def is_subword_valid(self, validated_word: str) -> bool:
        """
        Проверяет наличие слова в списке допустимых подслов.
        """
        return validated_word in self.subwords
