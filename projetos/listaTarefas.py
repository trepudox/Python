import time

nome_da_lista = ''
lista_tarefas = {}
contador_tarefa = 1
texto_inicio = "Lista de tarefas, você pode adicionar, remover, modificar e ver as tarefas da sua lista. " \
               "suas ações. "
ajuda = ["Comandos:\n\t",
         "'add': O comando 'add' serve para adicionar tarefas na lista.\n\t",
         "'list': O comando 'list' serve para listar todas as tarefas da lista.\n\t",
         "'mod': O comando 'mod' serve para modificar ou remover alguma das tarefas. Para removê-las, execute a função "
         "sem digitar nada.\n\t",
         "'!sair': O comando '!sair' serve para sair do programa.\n\t",
         "'!comandos': O comando '!comandos' serve para exibir este guia."]


def comandos(arg=ajuda):
    for xc in arg:
        yield xc


def inicio():
    global nome_da_lista
    print(texto_inicio, end='\n\n')
    time.sleep(0.25)
    nome_da_lista = input('Antes de começar, dê um nome para sua lista: ')
    print()
    time.sleep(0.25)
    for xi in comandos():
        print(xi, end='')
        time.sleep(0.25)
    print(end='\n\n')


def add(arg=lista_tarefas):
    global contador_tarefa
    entrada = input(f'Tarefa {contador_tarefa}: ').rstrip(' ')
    arg[f'Tarefa {contador_tarefa}'] = entrada
    if entrada != '':
        print('\nValor adicionado com sucesso.')
        contador_tarefa += 1
    else:
        print('\nNada foi digitado, logo nenhum valor foi adicionado.')
    return arg


def listar(arg=lista_tarefas):
    if len(arg) == 0:
        print('A lista de tarefas está vazia!')
    for xl, yl in arg.items():
        if yl != '':
            yield xl + ': ' + yl


def modificar(arg=lista_tarefas):
    global contador_tarefa
    if contador_tarefa == 1:
        print('Não existem tarefas para serem alteradas!')
        return
    while True:
        try:
            time.sleep(0.25)
            numero = int(input('Digite o número da tarefa: '))
            if contador_tarefa >= numero > 0:
                break
            else:
                time.sleep(0.25)
                print('\nPor favor, digite o número de alguma tarefa existente.\n')
        except ValueError:
            time.sleep(.25)
            print('\nPor favor, digite um número inteiro!\n')

    time.sleep(.25)
    arg[f'Tarefa {numero}'] = input(f'Digite o novo valor da Tarefa {numero}: ')


inicio()
while True:
    acao = input('Digite o que quer fazer: ').casefold()

    if acao == '!sair':
        break

    elif acao == '!comandos':
        print()
        for x in comandos():
            print(x, end='')
            time.sleep(0.25)
        print()

    elif acao == 'add':
        add()

    elif acao == 'list':
        print()
        for x in listar():
            print(x)
            time.sleep(0.25)

    elif acao == 'mod':
        print()
        modificar()
        print('Valor modificado com sucesso.')

    else:
        time.sleep(.25)
        print('\nEste comando não existe! Digite "!comandos" para ver todas as opções.')

    print()
    time.sleep(.25)

with open('listaTarefas.txt', 'w') as arquivo:
    arquivo.write(f'{nome_da_lista}:\n')
    for chave, valor in lista_tarefas.items():
        if valor != '':
            arquivo.write(f'\t{chave}: {valor}\n')
time.sleep(.25)
print('Fim do programa.')
