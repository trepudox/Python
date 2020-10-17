cigarro = int(input('Quantos cigarros você fuma por dia? Digite: '))
anos = int(input('Há quantos anos você fuma? Digite: '))

tempo1 = cigarro * 10 / 60 / 24 * anos * 365

print('Você perdeu {:.2f} dias de vida por causa dos {} cigarros que você fuma diariamente.'.format(tempo1, cigarro))

