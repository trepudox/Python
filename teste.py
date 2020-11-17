class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            print(f'{self._nome} já está ligado.')
        else:
            self._ligado = True
            print(f'{self._nome} agora está ligado.')

    def desligar(self):
        if self._ligado:
            self._ligado = False
            print(f'{self._nome} agora está desligado.')
        else:
            print(f'{self._nome} já está desligado.')

            