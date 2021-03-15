import math


def banki(d, h, p):
    x1 = math.pi * d ** 2 / 4
    x2 = math.pi * d * h
    x3 = 2 * x1 + x2
    e = math.ceil(x3 / p)
    return x1, x2, x3, e


d = int(input("Введите диаметр: "))
h = int(input("Введите высоту: "))
p = int(input("Введите площадь, которую можно окрасить одной банкой: "))

x1, x2, x3, e = banki(d, h, p)
print("Банок необходимо: {}".format(e))
