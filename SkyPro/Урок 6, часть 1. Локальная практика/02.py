"""
Ковер (псевдографика)
Напишите функцию draw_carpet(w, h), которая принимает ширину и высоту в клетках и генерирует “ковер” из псевдографики.
Вот, как меняется рисунок в зависимости от размера. Вы можете решить эту задачку, составив алгоритм,
а можете – методом проб и ошибок.
Используйте эти символы:
░ ▒ ▓
block_0 = u'\u2593'
block_1 = u'\u2592'
block_2 = u'\u2591'
"""


def draw_carpet(w: int, h: int) -> None:
    for i in range(h):
        for j in range(w):
            if j in [0, w - 1]:
                print(u'\u2591', end='')
            elif 0 < i < h - 1 and 1 < j < w - 2:
                print(u'\u2592', end='')
            else:
                print(u'\u2593', end='')
        print()


draw_carpet(10, 4)
