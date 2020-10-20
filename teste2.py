import time

data = time.localtime()

lista = [str(data.tm_mday), str(data.tm_mon), str(data.tm_year)]
resultado = '/'.join(lista)
print(resultado)