"""
Скрытое сообщение
Поздно вечером Алиса отправляет Борису сообщение, в котором часть символов заменена на цифры.
"Ага!" – говорит Александр Васильевич. - "Очень интересно!" Он заваривает кофе и пишет новую
программу для обратной замены.
Нужно заменить буквы обратно с помощью replace и получить сообщение.
"""

d = {
    '3': 'е',
    '4': 'ч',
    '6': 'б',
    '8': 'в',
    '9': 'д',
    '0': 'о',
}

message = 'Мн3 4у9ится, 4т0 кт0-т0 4итает с006щения!!! М0ж3т я 8се при9умала, н0 6у9ь на43ку, 0к?'

res = message
for encrypted, decrypted in d.items():
    res = res.replace(encrypted, decrypted)

print(res)
