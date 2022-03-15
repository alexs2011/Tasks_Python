"""
Анаграмма – слово (словосочетание), образованное путём перестановки букв, составляющих другое слово (или
словосочетание). Например, английские слова evil и live – это анаграммы.
На вход программе подаются два слова. Напишите программу, которая определяет, являются ли они анаграммами.
Формат входных данных
На вход программе подаются два слова, каждое на отдельной строке.
Формат выходных данных
Программа должна вывести YES если слова являются анаграммами и NO в противном случае.
"""


def anagram(first: str, second: str) -> bool:
    if len(first) != len(second):
        return False
    first_lst = list(first)
    second_lst = list(second)
    for ch in first_lst:
        if ch in second_lst:
            second_lst.remove(ch)
        else:
            return False
    return True


if __name__ == '__main__':
    print('YES' if anagram('aaab', 'baab') else "NO")
