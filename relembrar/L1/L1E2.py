dias = int(input("Digite quantos dias você viveu: "))

anos = dias / 365
meses = dias % 365 / 30
dias = dias % 365 % 30

print("Você viveu %d anos, %d meses e %d dias" % (anos, meses, dias))
