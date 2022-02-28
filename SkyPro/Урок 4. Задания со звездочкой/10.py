"""
Радиоротация
У вас есть список треков, которые играли сегодня на радио, в виде простого списка.
Составьте словарь, который показывает, сколько раз играл каждый трек.
"""

track_lst = [
    'Galibri & Mavik – Федерико Феллини',
    'DaBro - На Часах Ноль-Ноль',
    'Minelli - Rampampam',
    'DaBro - На Часах Ноль-Ноль',
    'Konfuz - Ратата',
    'Minelli - Rampampam',
    'DaBro - На Часах Ноль-Ноль',
]

res = {}

for track in track_lst:
    res[track] = res.setdefault(track, 0) + 1

print(res)
