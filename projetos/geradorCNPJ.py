from pythonProject.codigosPython.projetos.validadorDeCNPJ import cnpj_loop
from random import randint


def random_cnpj(formatado=False):
    cnpj = ''
    for x in range(12):
        cnpj += str(randint(0, 9))

    cnpj = cnpj_loop(cnpj)
    cnpj = cnpj_loop(cnpj, loop2=True)
    if formatado:
        return f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}'
    else:
        return cnpj


cnpj_aleatorio = random_cnpj(formatado=True)

print(cnpj_aleatorio)
# 04252011000110  |||  04.252.011/0001-10
