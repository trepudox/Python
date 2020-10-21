dic = {'Arroz': 10.0, 'Alface': 20.0, 'Feijão': 999.0}
condicao = ''
while True:
    if not condicao == '':
        print()
    condicao = input('Digite o que quer fazer, "V" para ver o preço de algum produto específico, "A" para adicionar'
                     'ou alterar produtos, "L" para listar todos os produtos, \n"D" para deletar algum produto, e '
                     '"!sair" para sair: ')

    if condicao.casefold() == '!sair':
        break

    elif condicao.casefold() == 'v':
        entrada = input('Digite o produto desejado para saber o preço: ').title()
        print(f'{entrada} custa R$', dic.get(entrada), '\n')

    elif condicao.casefold() == 'a':
        produtoadd = str(input('Digite o nome do produto: ')).title()
        dic[produtoadd] = float(input(f'Digite o valor de "{produtoadd}": '))
        print(f'Agora sua lista está assim: ')
        print(dic, '\n')

    elif condicao.casefold() == 'd':
        try:
            dic.pop(input('Digite o item que deseja deletar: ').title())
        except KeyError:
            print('Este produto não estava incluso na lista, impossível apagá-lo.')

    elif condicao.casefold() == 'l':
        for valores in dic.items():
            print(valores)


print('Fim do programa.')
