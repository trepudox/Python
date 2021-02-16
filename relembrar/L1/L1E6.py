from math import sqrt

x1 = int(input("Digite o valor de X1: "))
y1 = int(input("Digite o valor de Y1: "))
x2 = int(input("Digite o valor de X2: "))
y2 = int(input("Digite o valor de Y2: "))

d = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

print("A distância entre os dois pontos é de %.2f" % d)
