lst = [
    'Зашел: пришелец Хррзззз',
    'Вышел: пришелец Хррзззз',
    'Зашел: человек Архип',
    'Зашел: пришелец Гззззззр',
    'Вышел: пришелец Гззззззр',
    'Зашел: животное кот',
    'Вышел: животное кот',
    'Зашел: животное кот',
    'Вышел: животное кот',
    'Зашел: животное кот',
    'Вышел: животное кот',
]

# lst = ['Вышел: животное кот', 'Вышел: человек Архип']
d = {}  # если значение > 0 - кто-то зашёл; < 0 - вышел; = 0 - зашёл и вышел

for el in lst:
    data = el.split(': ')
    d[data[1]] = d.setdefault(data[1], 0)
    if data[0] == 'Зашел':
        d[data[1]] += 1
    else:
        d[data[1]] -= 1

res = [[], []]  # зашли и не вышли; вышли и не зашли
for name, status in d.items():
    if status > 0:
        res[0].append(name)
    if status < 0:
        res[1].append(name)

print('Зашли, но не вышли:')
if len(res[0]) == 0:
    print('никого')
for el in res[0]:
    print(el)

print('Вышли, но не зашли:')
if len(res[1]) == 0:
    print('никого')
for el in res[1]:
    print(el)
