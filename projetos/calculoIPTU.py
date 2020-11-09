def iptu(valor, residencial=True):
    mult, sub = 0, 0
    valor_negativo = False

    if 0 <= valor < 150000:
        if residencial:
            mult = 0.007
        else:
            mult = 0.011
        sub = 0
    elif 150000 <= valor < 300000:
        if residencial:
            mult = 0.009
        else:
            mult = 0.013
        sub = 300
    elif 300000 <= valor < 600000:
        if residencial:
            mult = 0.011
        else:
            mult = 0.015
        sub = 900
    elif 600000 <= valor < 1200000:
        if residencial:
            mult = 0.013
        else:
            mult = 0.017
        sub = 2100
    elif valor >= 1200000:
        if residencial:
            mult = 0.015
        else:
            mult = 0.019
        sub = 4500
    else:
        valor_negativo = True
        print('O valor do imóvel não pode ser negativo.')

    calculo = (valor * mult) - sub

    if valor_negativo:
        return
    else:
        return round(calculo, 1)


if __name__ == '__main__':
    try:
        entrada_tipo = input('Digite "1" caso seu imóvel seja residencial. Digite "2" para demais imóveis: ')
        if len(entrada_tipo) != 1:
            raise ValueError
        entrada_tipo = int(entrada_tipo)
        if entrada_tipo == 1:
            entrada = int(input('Digite aqui o valor do seu imóvel: '))
            if iptu(entrada) is not None:
                print('\nO valor do seu IPTU é de: R$ ' + str(iptu(entrada)), end='\n\n')
        elif entrada_tipo == 2:
            entrada = int(input('Digite aqui o valor do seu imóvel: '))
            if iptu(entrada, residencial=False) is not None:
                print('O valor do seu IPTU é de: R$ ' + str(iptu(entrada, residencial=False)), end='\n\n')
    except ValueError:
        print('\nDigite apenas "1" ou "2" para as opções de imóvel.\n')
    except TypeError:
        print('\nO valor do imóvel tem que ser um número inteiro, sem pontos ou alfacaracteres.\n')

    print('Fim do programa.')
