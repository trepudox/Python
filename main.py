entrada = input("Entrada de texto: ")
saida = entrada

if entrada[0] == " ":
    indice = -1
    for char in entrada:
        indice += 1
        if entrada[indice] == " ":
            continue
        else:
            saida = entrada[indice:]
            break
    else:
        print("Todos os dígitos eram espaços.")

try:
    if saida[-1] == " ":
        indice = -1
        for char in saida:
            if saida[indice] == " ":
                final = saida[:indice]
                indice -= 1
            else:
                break

except IndexError:
    print()


print(entrada)

print(saida)


lista = [x**2 for x in range(1, 10) if x % 2 == 1]

print(lista)
