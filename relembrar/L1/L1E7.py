a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
d = int(input("Digite o valor de D: "))
e = int(input("Digite o valor de E: "))
f = int(input("Digite o valor de F: "))

x = (c*e - b*f) / (a*e - b*d)
y = (a*f - c*d) / (a*e - b*d)

print("Os valores de X e Y são respectivamente: %d e %d." % (x, y))
