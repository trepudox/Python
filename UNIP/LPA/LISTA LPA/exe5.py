from math import sqrt

a = int(input('Digite um número para a: '))
b = int(input('Digite um número para b: '))
c = int(input('Digite um número para c: '))

delta = b**2 - 4*a*c

if delta < 0:
    print('A equação não possui raízes.')
else:
    raiz1 = (-b + sqrt(delta)) / 2 * a
    raiz2 = (-b - sqrt(delta)) / 2 * a

    print('x¹={:.2f}'.format(raiz1))
    print('x²={:.2f}'.format(raiz2))