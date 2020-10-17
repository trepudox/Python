x = input('Escolha um número: ')

if x.startswith('-'):
    x = x.replace('-', '')
    x = int(x)
    x = -x
elif x.isnumeric():
    x = int(x)
else:
    print('Por favor digite valores válidos.')

if x >= 5:
    print('O valor digitado é maior que o valor máximo.')



while x < 5:
    x+=1
    print(x)

print('Fim.')