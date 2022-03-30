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
        if 'download' in func.__name__:
            action = 'загрузки'
        elif 'parse' in func.__name__:
            action = 'парсинга'
        else:
            action = 'выполнения'
        print(f"Время {action}: {end - start:4f} c.")

        return val

    return wrapper
