from random import randint as numalet


def formula(x, cpfformula):
    conta = 11 - (x % 11)
    if conta > 9:
        cpfformula += '0'
        return cpfformula
    else:
        cpfformula += str(conta)
        return cpfformula


condicao = True

while condicao:
    cpf = ''

    for numero in range(9):
        cpf += str(numalet(0, 9))

    soma = 0

    contador = 10

    for num in cpf:
        soma += int(num) * contador
        contador -= 1

    cpf = formula(soma, cpf)

    contador = 11
    soma = 0

    for num2 in cpf:
        soma += int(num2) * contador
        contador -= 1

    cpf = formula(soma, cpf)

    sequencia = cpf == cpf[0] * len(cpf)

    if cpf and not sequencia:
        print('O CPF {}.{}.{}-{} é válido.'.format(cpf[0:3], cpf[3:6], cpf[6:9], cpf[9:]))
        condicao = False
