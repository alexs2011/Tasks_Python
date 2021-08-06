def unique_order(elements):
    res = [elements[0]]
    for el in elements:
        if el != res[-1]:
            res.append(el)
    return res


print(unique_order('AAAAABBBBCCDAAAABBB'))
print(unique_order('ABBCcAD'))
print(unique_order([1, 2, 2, 3, 3]))
