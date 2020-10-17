'''
Formatação de dados

floats
'''

numero = 10
numero2 = 3
divisao = numero / numero2

print('{:.2f}\n'.format(divisao))

'''
strings
'''

str1 = 'arroz'
str2 = 'azul'

print('{:T>10}  -  {:1<10}'.format(str1, str2))

print('{:@^10.2f}'.format(numero2))
