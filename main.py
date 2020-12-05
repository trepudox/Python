def for_e_indice(string: str):
    for indice, x in enumerate(string):
        print(str(indice) + ':', x)


for_e_indice('string teste')

lta = [x**2 for x in range(1,11)]
print(lta)