quantia_lista = int(input('Digite um número inteiro para definir o valor da lista: '))
lista = list(range(quantia_lista))
lista = [i+1 for i in lista]

dicionario_quadrado = {str(x+1): str(y**2) for x, y in enumerate(lista)}
entrada = ''
while True:
    entrada = input('Digite um número da lista para saber seu valor ao quadrado, para sair digite "!sair": ')
    if entrada.casefold() == '!sair':
        break

    print(f'O valor de {entrada} ao quadrado é {dicionario_quadrado.get(entrada)}\n')

print('Fim do programa')