"""
Классическая задача: скобки
Со стандартного ввода подается математическая формула. Если скобки в ней парные и
расставлены верно, верните True, иначе верните False
"""


def brackets_checker(formula: str) -> bool:
    left_brackets = [i for i, x in enumerate(formula) if x == '(']
    right_brackets = [i for i, x in enumerate(formula) if x == ')']
    if len(left_brackets) != len(right_brackets):
        return False
    for i in range(len(left_brackets)):
        if left_brackets[i] > right_brackets[i]:
            return False
    return True


formula = '(a + b) * (c - 1)'
print(brackets_checker(formula))
