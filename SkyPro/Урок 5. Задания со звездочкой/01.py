"""
Количество точек
В функцию передается количество точек по ширине, высоте и плотность пикселей. Если плотность не передана,
она считается равной 1. Посчитать физическое количество точек.
"""


def pixels_count(width: int, height: int, density: int = 1) -> int:
    return width * height * density


w, h, d = 480, 640, 2
print(pixels_count(w, h, d))
