from math import sqrt


def codifica(mensagem, num):
    cripto = ''
    for char in mensagem:
        cripto += chr(ord(char) + num)
    return cripto


print('\nPrograma de criptografia, insira corretamente a chave, o nome do arquivo onde a mensagem será guardada, e '
      'depois uma mensagem, para que ela seja criptografada. \nA mensagem não pode conter mais que 128 caracteres',
      end='\n\n')
while True:
    try:
        a = input('Digite a chave A: ')  # 0
        b = input('Digite a chave B: ')  # 9
        c = input('Digite a chave C: ')  # 0
        d = input('Digite a chave D: ')  # 0
        e = input('Digite a chave E: ')  # 0
        a, b, c, d, e = int(a), int(b), int(c), int(d), int(e)
    except ValueError:
        print('\nChave incorreta.')
        break

    delta = (((-b) ** 2 - 4 * a * c) + d) + e
    chave_correta = delta == 81

    if chave_correta:
        nome_arquivo = input('\nA mensagem será guardada em um arquivo texto. Digite o nome desse arquivo: ').lower()
        entrada = input('Agora, digite a mensagem a ser criptografada: ')
        if len(entrada) > 128:
            print('\nMensagem não pode conter mais que 128 caracteres.')
            break

        raiz = sqrt(delta)
        mensagem_criptografada = codifica(entrada, (int(raiz - 5)) * 100)

        print('\nA mensagem criptografada é a seguinte:\n' + mensagem_criptografada)

        with open(f'{nome_arquivo}.txt', 'w', encoding='UTF-8') as arquivo_txt:
            arquivo_txt.write(f'{mensagem_criptografada}')
        break

    else:
        print('\nChave incorreta.')
        break

print('\nFim do programa.')
