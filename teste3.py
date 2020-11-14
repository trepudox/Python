<<<<<<< HEAD
from math import sqrt

erro = False


def decodifica(criptografada, num):
    global erro
    descripto = ''
    for char in criptografada:
        try:
            descripto += chr(ord(char) - num)
        except ValueError:
            print('\nHá elementos não criptografados na mensagem. Impossível descriptografar.')
            erro = True
            return
    return descripto


print("\nPrograma de descriptografia, insira corretamente a chave e depois o nome do arquivo texto, que tenha uma "
      "mensagem criptografada pelo programa 'cripto'.\n(O arquivo texto precisa estar no mesmo diretório deste programa"
      " para que tudo funcione corretamente)", end='\n\n')
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
        entrada_arquivo = input('\nDigite o nome do arquivo a ser descriptografado: ').lower()
        try:
            with open(f'{entrada_arquivo}.txt', 'r', encoding='UTF-8') as arquivo_txt:
                leitura = arquivo_txt.read()
        except FileNotFoundError:
            print('\nO arquivo de texto não existe!')
            break

        raiz = int(sqrt(delta))

        mensagem_descriptografada = decodifica(leitura, (int(raiz) - 5) * 100)

        if erro:
            break

        print('\nA mensagem descriptografada é a seguinte:\n' + mensagem_descriptografada)
        break

    else:
        print('\nChave incorreta.')
        break

print('\nFim do programa.')
=======
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def chamar(self, pessoa):
        print(self.nome + ' chamou ' + pessoa.nome)


p1 = Pessoa('Marco', 18)
p2 = Pessoa('Albert', 20)

p1.chamar(p2)
>>>>>>> 1e9c93836a5cfb4c92e2df560ea4f1b6b4149b64
