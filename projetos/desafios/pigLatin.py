teste = 'uma frase de teste'


def pig_latin(entrada):

    lista_frase = entrada.split(' ')
    palavras_saida = lista_frase.copy()

    for index, palavras in enumerate(lista_frase):
        palavras_saida[index] = palavras[1:] + palavras[0] + 'ay'

    saida_real = ' '.join(palavras_saida)
    return saida_real


print(pig_latin(teste))
