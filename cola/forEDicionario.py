dicionario = {'Mano': 1, 'Raul': 2, 'Rafael': 3, }

a = dicionario.items()

for chave, valor in a:
    print("'{}' vale: {}".format(chave, valor))
