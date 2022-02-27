"""
Точное время 2
Алиса и Борис усовершенствовали шифр. Теперь звездочки означают час, а точки - 15-минутные интервалы. Например:
★★★. – это 3 часа 15 минут (3:15) ★★ – 2 часа 0 минут (2:00) ★★★★★... – 5 часов 45 минут (5:45 )
Напишите программу, которая переводит звездочки и точки во время.
"""

star_value = 1
dor_value = 15

user_input = input('Введите шифр: ')

star_count = user_input.count('*')
dot_count = user_input.count('.')

star_res = star_value * star_count if star_count > 0 else 0
dot_res = dor_value * dot_count if dot_count > 0 else '00'

print(f'{star_res}:{dot_res}')
