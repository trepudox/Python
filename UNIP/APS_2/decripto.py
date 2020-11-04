from math import sqrt

erro = False  # variável erro para identificar algum erro durante a execução da descriptografia


def decodifica(criptografada, num):
    global erro
    descripto = ''
    for char in criptografada:  # iteração nos caracteres da mensagem criptografada
        try:
            descripto += chr(ord(char) - num)  # tenta descriptografar cada caracter da mensagem
        except ValueError:  # se algum dos caracteres não estiver criptografado, cairá neste bloco except
            print('Há elementos não criptografados na mensagem. Impossível descriptografar.')
            erro = True
            return  # não retorna nada, apenas sai da função, pois houve erro
    return descripto  # retorna a mensagem descriptografada


print("Programa de descriptografia, insira corretamente a chave e depois uma mensagem, que foi criptografada pelo "
      "programa 'cripto', para que ela seja descriptografada.", end='\n\n')
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
        entrada = input('Digite a palavra ou frase a ser descriptografada: ')
        raiz = int(sqrt(delta))
        mensagem_descriptografada = decodifica(entrada, (int(raiz) - 5) * 100)

        if erro:  # erro capturado na função decodifica
            break
        print()
        print('A mensagem descriptografada é a seguinte:\n' + mensagem_descriptografada)
        with open('decripto.txt', 'w', encoding='UTF-8') as arquivo_txt:
            arquivo_txt.write(f'A última mensagem descriptografada foi:\n{mensagem_descriptografada}')
        break

    else:
        print('Chave incorreta.')
        break

print()
print('Fim do programa.')
