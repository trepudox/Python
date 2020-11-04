from math import sqrt


def codifica(mensagem, num):
    cripto = ''
    for char in mensagem:  # iteração nos carcteres da mensagem, para criptografá-los
        cripto += chr(ord(char) + num)
    return cripto


print('Programa de criptografia, insira corretamente a chave e depois uma mensagem, para que ela seja criptografada.',
      end='\n\n')
while True:
    try:  # bloco de try e except caso o usuario digite uma string
        a = input('Digite a chave A: ')  # 0
        b = input('Digite a chave B: ')  # 9
        c = input('Digite a chave C: ')  # 0
        print()
        a, b, c = int(a), int(b), int(c)
    except ValueError:  # caso uma das chaves seja uma string o programa irá parar imediatamente
        print('Chave incorreta.')
        break

    delta = (-b) ** 2 - 4 * a * c  # verificação da chave
    chave_correta = delta == 81  # verificação da chave

    if chave_correta:  # verificação da chave
        entrada = input('Digite a mensagem a ser criptografada: ')
        raiz = sqrt(delta)
        mensagem_criptografada = codifica(entrada, (int(raiz - 5)) * 100)
        print()
        print('A mensagem criptografada é a seguinte:\n' + mensagem_criptografada)
        with open('cripto.txt', 'w', encoding='UTF-8') as arquivo_txt:
            arquivo_txt.write(f'A última mensagem criptografada foi:\n{mensagem_criptografada}')
        break
    else:
        print('Chave incorreta.')
        break

print()
print('Fim do programa.')
