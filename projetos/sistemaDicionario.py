dicionario = {}

arquivo = open('sistemaDicionariotxt.txt', 'w+')

print('Comandos do programa:\n"V" para ver uma chave específica\n"A" para adicionar uma chave\n"E" para excluir uma '
      'chave\n"I" para ver todos os valores do dicionario\n')

while True:
    acao = str(input('Digite qual comando quer executar, "!comandos" para ver os comandos ou "!sair" para sair.')).casefold()

    if len(acao) != 1 and 'v' != acao and acao != 'a' and acao !=:
        print('Digite apenas comandos existentes para o funcionamento correto do programa.')

    if 1:
        dicionario[input('Digite o nome da chave: ')] = input('Digite o valor da chave: ')

