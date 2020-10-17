string = ''
lista = []

while True:
    string = input('Digite uma palavra para estar incluída na lista, digite "!sair" para sair: ')
    if string.casefold() == "!sair":
        break

    lista.append(string)

for palavra in lista:
    indice = 0

    for letra in palavra:
        print('"' + letra + '"' + ' - {}'.format(indice))
        indice += 1

    print()
