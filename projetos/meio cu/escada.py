string = input('Digite uma palavra: ')
x = 1

for letra in string:

    print(string[:x])
    x += 1

    if x > len(string):
        break

for letraX in string:

    print(string[0:x-2])
    x -= 1

    if x < 0:
        break
