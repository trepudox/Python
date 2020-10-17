def par(x):
    if x % 2 == 0:
        return True
    else:
        return False

def parString(y):
    if par(y):
        return 'sim'
    else:
        return 'nao'

def oMaior(x,y):
    if x > y:
        return x
    if x < y:
        return y
    else:
        return x

def areaTriang(base, altura):
    area = (base * altura) / 2
    return area

#print(par(2))

def cabecalho(str):
    print(str)
    print('-' * len(str))

ex = 1
def muda():
    ex = 2
    print(ex)

print(ex)
muda()
print(ex)
print(globals())