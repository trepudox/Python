import math

x = float(input('Digite o valor de X: '))
y = float(input('Digite o valor de Y: '))

soma = x + y
sub = x - y
mult = x * y
div = x / y
raiz = math.sqrt(x * y)
cubo = math.pow((2*x + y/3),3)
quad = 4*(1/x*y)


print("\nA soma de {} e {} é igual a {:.2f}".format(x, y, soma))

print('\nA subtração entre {} e {} é igual a {:.2f}'.format(x, y, sub))

print('\nA multiplicação entre {} e {} é igual a {:.2f}'.format(x, y, mult))

print('\nA divisão entre {} e {} é igual a {:.2f}'.format(x, y, div))

print('\nA raíz quadrada do produto de {} e {} é igual a {:.2f}'.format(x, y, raiz))

print('\nO cubo do dobro de {} mais um terço de {} é igual a {:.2f}'.format(x, y, cubo))

print('\nO quádruplo do inverso do produto de {} e {} é igual a {:.2f}'.format(x, y, quad))