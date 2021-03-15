

def formula_1(x1, y1, x2, y2):
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    return k, b
z = int(input("Введите x1\n"))
m = int(input("Введите x2\n"))
n = int(input("Введите y1\n"))
u = int(input("Введите y2\n"))

k, b = formula_1(z, m, n, u)
print("Координаты точки А(x1;y1)\n x1 = ",z,"\n y1 = " ,m, "\n")
print("Координаты точки А(x2;y2)\n x2 = ",n,"\n y1 = " ,u, "\n")
print("Уравнение прямой, проходящей через эти точки\n y=",k,"*x+",b)



