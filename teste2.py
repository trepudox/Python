class Animal:
    def __init__(self, sexo, patas, olhos):
        self.sexo = sexo
        self.patas = patas
        self.olhos = olhos
        self.vivo = True

    def estiver_vivo(self):
        if self.vivo:
            return True
        else:
            return False


class Cachorro(Animal):
    def __init__(self, sexo, patas, olhos, nome, idade, cor, raca):
        super.__init__(sexo, patas, olhos)
        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.raca = raca

    def caracteristicas(self):
        print(f'Características de {self.nome}')


if __name__ == '__main__':
    cao1 = Cachorro('Macho', 4, 2, 'Max', 2, 'Preto', 'Vira-Lata')