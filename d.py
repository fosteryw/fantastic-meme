def formula_2(x3):
    w = x3 ** 2
    s = x3 ** 0.5
    return w, s


xy = 999
w, s = formula_2(xy)
print(w, s)


def stroka(stra):
    if not isinstance(stra, str):
        return 'Error'
    u = stra[3::5]
    return u


print(
    stroka('asdasf'))

print("sdffd".replace('ff', '89898'))
print("as{}d".format(w))

def formula_1(x1, y1, x2, y2):
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    return k, b


o = 8
k, b = formula_1(1, 3, 5, o)
print(k, b)



