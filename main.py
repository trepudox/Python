lista = []
condicao = True


def pulalinha():
    print()


def add():
    try:
        nome = input('Nome: ')
        valor = int(input('Valor: '))
        lista.append((nome, valor))
    except ValueError:
        print('\nValor precisa ser um número\n')

    pulalinha()


def rmv():
    try:
        entrada = int(input('Número do item a ser removido: '))
        lista.pop(entrada)
    except IndexError:
        print('\nNão há nenhum item com este índice.')
    except ValueError:
        print('\nApenas números são validos.')

    pulalinha()


def ver():
    if len(lista) == 0:
        print('\nLista vazia.')
    print()
    for indice, item in enumerate(lista):
        print('Item', str(indice) + ':', item[0] + ',', item[1])
    pulalinha()


def sair():
    global condicao
    print('\nFim do programa.')
    condicao = False


def com():
    pulalinha()
    print('"add" - adiciona itens na lista')
    print('"rmv" - remove itens da lista de acordo com a sua posição')
    print('"ver" - mostra a lista')
    print('"sair" - sai do programa')
    print('"com" - mostra os comandos')
    pulalinha()


print('Digite "com" para ver os comandos.\n')

while condicao:
    escolha = input('Digite o comando que quer executar: ').lower()

    if escolha == 'add':
        add()

    elif escolha == 'rmv':
        rmv()

    elif escolha == 'ver':
        ver()

    elif escolha == 'com':
        com()

    elif escolha == 'sair':
        sair()

    else:
        print()
        print('Comando inexistente')
        print()


with open('arquivo.txt', 'w') as arquivo:
    for indice, item in enumerate(lista):
        arquivo.write(f"Item {indice}: {item[0]}, {item[1]}")
