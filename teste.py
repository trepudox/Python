class Cachorro:
    def __init__(self, cor, sexo, porte_fisico, nome='Cachorro'):
        self.nome = nome
        self.cor = cor
        self.sexo = sexo
        self.porte_fisico = porte_fisico

    def latir(self):
        print(f'{self.nome} latiu.')


tarzan = Cachorro('preto', 'macho', 'forte', nome='Tarzan')
mel = Cachorro('caramelo', 'fêmea', 'fino')

tarzan.latir()
mel.latir()
