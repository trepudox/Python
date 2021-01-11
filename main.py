entrada = input("Texto de entrada ->")
contador = 0
letra = "a"

for x in entrada:
    if x == letra:
        contador += 1
else:
    print(f"A letra '{letra}' estava {contador} vezes na frase.")