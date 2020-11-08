class Gato:
    def __init__(self, patas, cor, tamanho, nome='Gato'):
        self.patas = patas
        self.cor = cor
        self.tamanho = tamanho
        self.nome = nome

    def miar(self):
        print(self.nome + ' miou. Miau!')


jaspion = Gato(4, 'preto', 'pequeno', 'Jaspion')

jaspion.miar()
