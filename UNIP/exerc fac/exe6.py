produto = int(input('Digite o código do produto(entre 1 e 5): '))

if produto == 1:
    preco = 10
elif produto == 2:
    preco = 18
elif produto == 3:
    preco = 23
elif produto == 4:
    preco = 26
elif produto == 5:
    preco = 31
else:
    preco = 0

if preco == 0:
    print('Digite um código de produto válido')
else:
    print('O preço do produto é R$ {}'.format(preco))