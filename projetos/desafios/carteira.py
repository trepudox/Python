entrada_nome = input()
num_agentes = int(input())
entrada_lista = input()

lista = entrada_lista.split(' ')
lista.append(entrada_nome)
lista.sort()

# print(lista)
# print(type(lista))

contador = 1

for x in lista:
    contador += 1
    if x == entrada_nome:
        break

if num_agentes > len(lista):
    num_agentes = len(lista)

try:
    conta = int(round((contador / num_agentes)) * 20)
except ZeroDivisionError:
    conta = 0

print(conta)
