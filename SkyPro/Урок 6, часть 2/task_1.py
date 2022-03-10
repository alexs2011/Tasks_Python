import random
import os


def read_words(filename: str = 'data/words.txt') -> list[str]:
    """
    Считывает все слова из файла.
    """
    with open(filename, 'r', encoding='utf-8') as f_input:
        res_lst = [x.strip() for x in f_input.readlines()]
    return res_lst


def read_history_statistic(filename: str = 'data/history.txt') -> tuple[int, int]:
    """
    Считывает информацию из файла истории и определяет число прошедших игр и максимальный рекорд.
    """
    max_score = 0
    count_games = 0
    with open(filename, 'r', encoding='utf-8') as f_input:
        for line in f_input:
            data = line.strip().split()
            if int(data[1]) > max_score:
                max_score = int(data[1])
            count_games += 1
    return count_games, max_score


def update_history_statistic(name: str, score: int, filename: str = 'data/history.txt') -> None:
    """
    Добавляет статистику новой игры в файл с историей.
    """
    with open(filename, 'a', encoding='utf-8') as f_output:
        if os.stat(filename).st_size == 0:  # если файл пуст
            f_output.write(f'{name} {score}')
        else:
            f_output.write(f'\n{name} {score}')


if __name__ == '__main__':
    user_name = input("Введите ваше имя: ")

    words = read_words()

    score = 0

    for word in words:
        shuffled_word = list(word)
        random.shuffle(shuffled_word)
        print(f'\nУгадайте слово: {"".join(shuffled_word)}')
        user_input = input()
        if user_input == word:
            print('Верно! Вы получаете 10 очков.')
            score += 10
        else:
            print(f'Неверно! Верный ответ – {word}.')

    print(f'\nВаш счёт: {score}')

    update_history_statistic(user_name, score)

    statistic = read_history_statistic()

    print(f'\nВсего игр сыграно: {statistic[0]}')
    print(f'Максимальный рекорд: {statistic[1]}')
