base = int(input('Digite a base: '))
altura = int(input('Digite a altura: '))
area = 10
print(area)


def areaT():
    global base, altura, area
    area = (base * altura) / 2


areaT()
print(area)
