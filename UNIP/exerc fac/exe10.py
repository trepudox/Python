#Faça um programa exibir apenas o números pares entre 0 e um número digitado pelo usuário
x = input('Digite um número: ')

if x == 0 or '.' in x:
    print('O número digitado não pode ser 0 e nem ser decimal.')
else:
    x = int(x)
    while x != 0:
        if x > 0:
            if x % 2 == 0:
                print(x)
                x -= 1
            else:
                x -= 1
        else:
            if x % 2 == 0:
                print(x)
                x += 1
            else:
                x += 1

print('Fim do programa.')