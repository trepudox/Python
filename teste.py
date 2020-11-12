import time

sem_erro = True

while sem_erro:
    for x in range(10):
        print('#' * x)
        time.sleep(0.75)
    else:
        sem_erro = False
else:
    print('a')
