anoDig = int(input('Digite um ano para verificar se o mesmo é bissexto: '))

if anoDig % 400 == 0 or (anoDig % 4 == 0 and anoDig % 100 != 0):
    print('O ano de {} é bissexto'.format(anoDig))
else:
    print('O ano de {} não é bissexto'.format(anoDig))