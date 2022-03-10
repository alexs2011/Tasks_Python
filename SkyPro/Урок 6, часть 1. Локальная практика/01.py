"""
Обработка ошибок (словари)
Существует словарь ошибок для пользователя в системе.
Напишите функцию get_errors(error, error, error ...), которая вернет набор ошибок списком,
в ответ на список аргументов, который был передан.
"""


def get_errors(*args: str) -> list[str]:
    return [dict_errors[x] for x in args]


dict_errors = {
    'out': 'Вы вышли из системы ',
    'noaccess': 'У вас нет доступа в этот раздел',
    'unknown': 'Неизвестная ошибка',
    'timeout': 'Система долго не отвечает',
    'robot': 'Ваши действия похожи на робота',
}

print(get_errors('out', 'noaccess', 'timeout'))
