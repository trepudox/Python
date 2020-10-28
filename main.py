def formula(num):
    x = 11 - (num % 11)
    if x > 9:
        return '0'
    else:
        return str(x)


def cnpj_loop(cnpj, loop2=False):
    if loop2:
        num = 6
        add = 5
    else:
        num = 5
        add = 4

    conta = 0

    for x, y in enumerate(range(num, 1, -1)):
        conta += (int(cnpj[x]) * y)

    for x, y in enumerate(range(9, 1, -1)):
        conta += (int(cnpj[x + add]) * y)

    return cnpj + formula(conta)


while True:
    entrada_usuario = input('Digite o CNPJ sem pontos, traços e barras: ')  # 04252011000110  |||  04.252.011/0001-10
    if len(entrada_usuario) != 14 or not entrada_usuario.isnumeric():
        print('\nO CNPJ deve conter 14 dígitos numéricos, sem usar traços, pontos, barras e letras.\n')
    else:
        break

cnpj_original = entrada_usuario
cnpj_calculo = cnpj_original[:-2]

cnpj_calculo = cnpj_loop(cnpj_calculo)
cnpj_calculo = cnpj_loop(cnpj_calculo, loop2=True)

cnpj_valido = cnpj_calculo == cnpj_original

if cnpj_valido:
    print(f'O CNPJ {cnpj_calculo[:2]}.{cnpj_calculo[2:5]}.{cnpj_calculo[5:8]}/{cnpj_calculo[8:12]}-{cnpj_calculo[12:]} é válido.')
else:
    print(f'O CNPJ {cnpj_calculo[:2]}.{cnpj_calculo[2:5]}.{cnpj_calculo[5:8]}/{cnpj_calculo[8:12]}-{cnpj_calculo[12:]} é inválido.')
