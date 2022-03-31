import time
import functools


def timer(func):
    """
    Печатает время выполнения декорированной функции.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        val = func(*args, **kwargs)
        end = time.time()
        action = 'выполнения'
        if 'download' in func.__name__:
            action = 'загрузки'
        elif 'parse' in func.__name__:
            action = 'парсинга'

        print(f"Время {action}: {end - start:4f} c.")

        return val

    return wrapper


def console_log(_func=None, *, info_str=None):
    def dec(func):
        def wrapper(*args, **kwargs):

            val = func(*args, **kwargs)

            return val
        return wrapper
    if _func is None:
        return dec
    else:
        return dec(_func)
