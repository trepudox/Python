cript_letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z', 'á', 'à', 'â', 'ã', 'é', 'ê', 'í', 'ó', 'õ', 'ô', 'ú', 'ç', ',', '.',
                ' ', '(', ')', ':', '!', '?']

cript_codigo = ['#3', 'ä0', '[ü', '¢2', '4¬', 'ý"', '1/', '&ñ', '5*', '/^', '*=', '6]', '+¨', '@~', '<=', '0;',
                '~2', '%7', '8$', '")', '9_', '(1', 'ý@', '¬2', '°&', '*[', '3|', '4=', '-ö', '_ü', 'ñ/', '5.',
                '°6', '~°', '@_', '^&', 'ª^', '*/', '|,', '|.', '£{', '0"', '"0', '|:', '|!', '|?']

mensagem = ''
cont = 0
condicao = ''
arquivo_cripto = open('texto_cripto.txt', 'w+')
arquivo_descripto = open('texto_descripto.txt', 'w+')


while condicao.casefold() != '!sair!'.casefold():
    cont = 0
    mensagem = ''

    condicao = input('Digite "c" para criptografar uma mensagem, "d" para descriptografar uma mensagem, ou "!sair!" '
                     'para sair do programa. Digite aqui: ')

    if condicao.casefold() == 'c'.casefold():
        mensagem = input('Digite sua mensagem para ser criptografada, por favor, se quiser incluir números, digite '
                         'por extenso: ')
        mensagem = mensagem.casefold()

        for char in mensagem:
            if cont < len(mensagem):
                mensagem = mensagem.replace(mensagem[cont], cript_codigo[cript_letras.index(mensagem[cont])], 1)
                cont += 2
            else:
                break

        arquivo_cripto.write(mensagem)
        arquivo_cripto.seek(0)
        print(arquivo_cripto.read())

    elif condicao.casefold() == 'd'.casefold():
        mensagem = input('Digite sua mensagem para ser descriptografada, por favor, se quiser incluir números, '
                         'digite por extenso: ')
        cont = 1

        for chars in mensagem:
            if cont < len(mensagem):
                mensagem = mensagem.replace((mensagem[cont - 1] + mensagem[cont]), cript_letras[cript_codigo.index((mensagem[cont - 1] + mensagem[cont]))], 1)
                cont += 1
            else:
                break

        arquivo_descripto.write(mensagem)
        arquivo_descripto.seek(0)
        print(arquivo_descripto.read())

    elif condicao.casefold() == '!sair!'.casefold():
        break

    else:
        print('Por favor digite um dos comandos citados para que o programa funcione corretamente.')

arquivo_cripto.close(), arquivo_descripto.close()
print('Fim do programa.')

#/^~°5*#3£{ý"4¬%7
#jóia fer
