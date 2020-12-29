entrada = input()
pontos = ['!', ',', '.', '?', ';', ':']
for x in pontos:
    entrada = entrada.replace(x, '')

palavras = entrada.split(' ')

soma = 0
contador = 0

for plv in palavras:
    soma += len(str(plv))
    contador += 1
else:
    media = soma / contador

media_for_inteira = soma % contador == 0

if media_for_inteira:
    print(int(media))
else:
    print(int(media) + 1)
