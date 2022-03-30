import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        val = func(*args, **kwargs)
        end = time.time()
        if 'download' in func.__name__:
            print(f"Время загрузки: {end - start} c.")
        elif 'parse' in func.__name__:
            print(f"Время парсинга: {end - start} c.")
        else:
            print(f"Время выполнения: {end - start} c.")

        return val

    return wrapper
