import random
import requests

from classes.BasicWord import BasicWord
from classes.Player import Player

FINISH_GAME = ['стоп', 'stop']


def load_random_word(url: str) -> BasicWord:
    def load_data(url: str) -> list[dict]:
        try:
            data = requests.get(url)
        except requests.exceptions.ConnectionError:
            raise ConnectionError(f"Отсутствует подключение к интернету.")
        if data.status_code != 200:
            raise ConnectionError("Удалённый ресурс не отвечает или не существует.")
        if 'application/json' not in (cont_type := data.headers.get('Content-Type')):
            raise requests.exceptions.JSONDecodeError(f"Результат запроса не JSON: {cont_type}")

        data = data.json()

        valid_keys = {'word', 'subwords'}
        for el in data:
            if set(el.keys()) != valid_keys:
                raise ValueError(f"Неверные данные: {el.keys()}")
        return data

    words = load_data(url)
    random_word = random.choice(words)
    return BasicWord(random_word['word'], random_word['subwords'])


def generate_player(name: str) -> Player:
    return Player(name)
