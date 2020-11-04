from math import sqrt


def codifica(mensagem, num):
    cripto = ''
    # iteração nos caracteres da mensagem, para criptografá-los
    for char in mensagem:
        cripto += chr(ord(char) + num)
    return cripto


print('\nPrograma de criptografia, insira corretamente a chave, o nome do arquivo onde a mensagem será guardada, e '
      'depois uma mensagem, para que ela seja criptografada. \nA mensagem não pode conter mais que 128 caracteres',
      end='\n\n')
while True:
    # bloco de try e except caso o usuario digite uma string
    try:
        a = input('Digite a chave A: ')  # 0
        b = input('Digite a chave B: ')  # 9
        c = input('Digite a chave C: ')  # 0
        a, b, c = int(a), int(b), int(c)
    # caso uma das chaves seja uma string o programa irá parar imediatamente
    except ValueError:
        print('\nChave incorreta.')
        break
    # verificação da chave
    delta = (-b) ** 2 - 4 * a * c
    chave_correta = delta == 81
    if chave_correta:
        # entrada do usuário
        nome_arquivo = input('\nA mensagem será guardada em um arquivo texto. Digite o nome desse arquivo: ').lower()
        entrada = input('Agora, digite a mensagem a ser criptografada: ')
        # verificação de quantos caracteres há na mensagem
        if len(entrada) > 128:
            print('Mensagem não pode conter mais que 128 caracteres.')
            break

        # conta da raíz de delta
        raiz = sqrt(delta)
        # função para criptografar a mensagem
        mensagem_criptografada = codifica(entrada, (int(raiz - 5)) * 100)

        print('\nA mensagem criptografada é a seguinte:\n' + mensagem_criptografada)
        # cria ou abre o arquivo em UTF-8 e modo de escrita, salvando a mensagem e sobrescrevendo qualquer dado
        # que estivesse já estivesse escrito
        with open(f'{nome_arquivo}.txt', 'w', encoding='UTF-8') as arquivo_txt:
            arquivo_txt.write(f'{mensagem_criptografada}')
        break
    # caso as chaves A, B e C sejam números inteiros, porém delta não é igual a 81
    else:
        print('Chave incorreta.')
        break

print('\nFim do programa.')
