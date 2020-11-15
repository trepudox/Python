from math import sqrt
from time import sleep


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
    # bloco de try e except caso o usuario digite uma string nas chaves
    try:
        a = input('Digite a chave A: ')  # 0
        b = input('Digite a chave B: ')  # 9
        c = input('Digite a chave C: ')  # 0
        d = input('Digite a chave D: ')  # 0
        e = input('Digite a chave E: ')  # 0
        a, b, c, d, e = int(a), int(b), int(c), int(d), int(e)
    # caso uma das chaves seja uma string o programa irá parar imediatamente
    except ValueError:
        print('\nChave incorreta.')
        break

    # verificação da chave, a verificação é feita através da conta do delta, da fórmula de bhaskara, adicionamos dois
    # fatores, o D e o E, para dificultar o acesso a criptografia e descriptografia
    delta = (((-b) ** 2 - 4 * a * c) + d) + e
    chave_correta = delta == 81

    if chave_correta:
        # entrada do usuário
        nome_arquivo = input('\nA mensagem será guardada em um arquivo texto. Digite o nome desse arquivo: ').lower()
        entrada_mensagem = input('Agora, digite a mensagem a ser criptografada: ')
        # verificação de quantos caracteres há na mensagem
        if len(entrada_mensagem) > 128:
            print('\nMensagem não pode conter mais que 128 caracteres.')
            break

        # conta da raíz de delta, o número é usado para alterar os caracteres
        raiz = sqrt(delta)
        # função para criptografar a mensagem
        mensagem_criptografada = codifica(entrada_mensagem, (int(raiz - 5)) * 100)

        print('\nA mensagem criptografada é a seguinte:\n' + mensagem_criptografada)

        # cria ou abre o arquivo em UTF-8 e modo de escrita, salvando a mensagem e sobrescrevendo qualquer dado
        # que estivesse já estivesse escrito

        with open(f'{nome_arquivo}.txt', 'w', encoding='UTF-8') as arquivo_txt:
            arquivo_txt.write(f'{mensagem_criptografada}')
        break

    # caso as chaves A, B e C sejam números inteiros, porém delta não é igual a 81
    else:
        print('\nChave incorreta.')
        break

print('\nFim do programa.')
sleep(7.5)


# !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ // 32 ao 125
# áâãäåæçèéêëìíîïðñòóôõö÷øùúû // 225 ao 252
