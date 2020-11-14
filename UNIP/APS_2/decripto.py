from math import sqrt
from time import sleep

# variável erro para identificar algum possível erro durante a execução da descriptografia
erro = False


def decodifica(criptografada, num):
    global erro
    descripto = ''
    # iteração nos caracteres da mensagem criptografada
    for char in criptografada:
        # tenta descriptografar cada caracter da mensagem
        try:
            descripto += chr(ord(char) - num)
        # se algum dos caracteres não estiver criptografado pelo programa cripto, cairá neste bloco except
        except ValueError:
            print('\nHá elementos não criptografados na mensagem. Impossível descriptografar.')
            # retorna None, erro agora se torna True e sai da função, pois ocorreu um erro erro
            erro = True
            return
    # retorna a mensagem descriptografada
    return descripto


print("\nPrograma de descriptografia, insira corretamente a chave e depois o nome do arquivo texto, que tenha uma "
      "mensagem criptografada pelo programa cripto. \n(O arquivo texto precisa estar no mesmo diretório deste programa "
      "para que tudo funcione corretamente).", end='\n\n')
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
        entrada_arquivo = input('\nDigite o nome do arquivo a ser descriptografado: ').lower()
        try:
            # abre o arquivo em UTF-8 e modo de leitura. Caso o arquivo não exista, o programa para e avisa o usuário
            with open(f'{entrada_arquivo}.txt', 'r', encoding='UTF-8') as arquivo_txt:
                leitura = arquivo_txt.read()
        except FileNotFoundError:
            print('\nO arquivo de texto não existe!')
            break

        # calcula a raíz de delta, o número é usado para reverter a alteração dos caracteres
        raiz = int(sqrt(delta))

        # função para descriptografar a mensagem
        mensagem_descriptografada = decodifica(leitura, (int(raiz) - 5) * 100)

        # bloco if para verificar se houve erro durante a execução da função
        if erro:
            break

        # printa na tela a mensagem descriptografada
        print('\nA mensagem descriptografada é a seguinte:\n' + mensagem_descriptografada)
        break

    # caso as chaves A, B e C sejam números inteiros, porém delta não é igual a 81
    else:
        print('\nChave incorreta.')
        break

print('\nFim do programa.')
sleep(7.5)
