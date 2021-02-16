duracao = int(input("Digite a duração do evento na fábrica: "))

horas = duracao / 3600
minutos = duracao % 3600 / 60
segundos = duracao % 3600 % 60

print("O evento na fábrica durou %d horas, %d minutos e %d segundos" % (horas, minutos, segundos))
