class Animal:
    def __init__(self, raca, cor, nome):
        self.raca = raca
        self.cor = cor
        self.nome = nome

    def latir(self):
        print(self.nome + ' latiu.')


cachorro = Animal('yorkshire', 'mesclado', 'dolfo')
cachorro.latir()