"""
Шифрование сдвигом (строки)
Один из простейших алгоритмов шифрования – замена буквы на следующую, например “а” заменяется на “б”, “б” заменяется
на “в”, а “я” заменяется на “а”.
1. Напишите функцию shift_encode(string) которая шифрует строку
2. Напишите функцию shift_decode(string) которая дешифрует строку обратно
"""


def shift_encode(string: str) -> str:
    res = ''
    for ch in string:
        ch_code = ord(ch)
        if 1040 <= ch_code <= 1070 or 1072 <= ch_code <= 1102:
            res += chr(ch_code + 1)
        elif ch_code == 1071:
            res += chr(1040)
        elif ch_code == 1103:
            res += chr(1072)
        else:
            res += ch
    return res


def shift_decode(string: str) -> str:
    res = ''
    for ch in string:
        ch_code = ord(ch)
        if 1041 <= ch_code <= 1071 or 1073 <= ch_code <= 1103:
            res += chr(ch_code - 1)
        elif ch_code == 1040:
            res += chr(1071)
        elif ch_code == 1072:
            res += chr(1103)
        else:
            res += ch
    return res


message = 'А-Я, а-я. Тест шифрования'
crypted_message = shift_encode(message)
decrypted_message = shift_decode(crypted_message)

print(crypted_message)
print(decrypted_message)
