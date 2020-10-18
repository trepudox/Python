lista = [i + 1 for i in range(10)]

dicionario = {x: y for x in lista for y in [0, input(f'Digite o valor da chave {x}: ')]}

print(dicionario)