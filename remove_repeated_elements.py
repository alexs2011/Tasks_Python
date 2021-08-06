def unique_order(elements):
    res = []
    unique_elem = None
    for el in elements:
        if el != unique_elem:
            unique_elem = el
            res.append(el)
    return res


print(unique_order('AAAAABBBBCCDAAAABBB'))
print(unique_order('ABBCcAD'))
print(unique_order([1, 2, 2, 3, 3]))
