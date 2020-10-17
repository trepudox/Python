import time

for x in range(0, 10):
    time.sleep(1)
    print('antes do sleep')
    time.sleep(1)
    print('entrando em um sleep de 10 segundos')

    for segundos in range(10):
        time.sleep(1)
        print(segundos+1)

    print('fim do sleep')
    print()