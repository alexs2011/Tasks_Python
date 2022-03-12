"""
Лидар
В файле furry_road.txt указываются плитки дороги шириной 5 клеток. Напишите автопилот, который едет сверху вниз и
на каждый ряд выбирает, куда ехать: left, right, stay. При наличии нескольких вариантов машина держится правой стороны
(на картинке она слева). Программа должна считывать файл построчно.
"""

obstacle = u'\u2593'
clear_path = u'\u2591'

car_pos_idx = 2

print(f'  X   {car_pos_idx + 1}')

with open('furry_road.txt', 'r', encoding='utf-8') as f_in:
    # prev_row нужен для проверки того, было ли в предыдущем ряду препятствие в том направлении, в котором мы хотим
    #                                                     X
    # переместиться. Это нужно для того, чтобы в ситуации ░ ▓ ░ ▓ ░ машина не могла проехать по диагонали.
    #                                                     ▓ ░ ▓ ░ ░
    prev_row = clear_path * 5

    for row in f_in:
        row = row.strip().split()
        print(''.join(row), end=' ')
        if row[car_pos_idx] == obstacle:
            if car_pos_idx > 0 and row[car_pos_idx - 1] == clear_path and prev_row[car_pos_idx - 1] == clear_path:
                print(f'right->{car_pos_idx}')
                car_pos_idx -= 1
            elif car_pos_idx < len(row) - 1 and row[car_pos_idx + 1] == clear_path \
                    and prev_row[car_pos_idx + 1] == clear_path:
                print(f'left->{car_pos_idx + 2}')
                car_pos_idx += 1
            else:
                print('stop')
                break
        else:
            print('stay')

        prev_row = row
