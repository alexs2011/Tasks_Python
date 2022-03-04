"""
Номера запрещены
Для безопасности пользователей в некоторых сервисах запрещено отправлять в личных сообщениях номера телефонов.
Со стандартного ввода подается текст сообщения. Функция должна вернуть, встречается ли номер телефона в строке.
Номер телефона не может содержать пробелы, но может содержать + - ( )
"""


def is_phone_in_string(string: str) -> bool:
    words = string.split()
    for word in words:
        tmp = word.replace('+', '').replace('-', '').replace('(', '').replace(')', '')
        if tmp.isdigit():
            return True
    return False


string = 'text +7(999)111-22-33'
print(is_phone_in_string(string))
