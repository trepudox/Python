class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

    bracos = 2
    pernas = 2
    maos = 2

    def quantos(self):
        if self.bracos != 2:
            print('oh meu deus')


p1 = Pessoa('Marco', 18, 1.65, 58)
p2 = Pessoa('Marco', 18, 1.65, 58)

p2.bracos = 1

p2.quantos()

print(p1.bracos)
print(p2.bracos)