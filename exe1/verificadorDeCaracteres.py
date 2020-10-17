palavra = input('Digite uma palavra: ')
char = input('Digite um caracter ou uma sequência de caracteres: ')

#if char.lower() in palavra.lower():
#    print('O(s) caracter(es) {} está(ão) presente(s) em {}'.format(char, palavra))
#else:
#    print('O(s) caracter(es) {} não está(ão) presente(s) em {}'.format(char, palavra))

if char.__len__() > 0 or palavra.__len__() > 0:
    if char.__len__() == 1:
        if char.lower() in palavra.lower():
            print('O caracter \'{}\' está presente em \'{}\''.format(char.lower(), palavra.lower()))
        else:
            print('O caracter \'{}\' não está presente em \'{}\''.format(char.lower(), palavra.lower()))
    elif char.__len__() > 1:
        if char.lower() in palavra.lower():
            print('A sequência de caracteres \'{}\' está presente em \'{}\''.format(char.lower(), palavra.lower()))
        else:
            print('A sequência de caracteres \'{}\' não está presente em \'{}\''.format(char.lower(), palavra.lower()))
else:
    print('Por favor digite dados válidos.')
