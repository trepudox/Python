import time

while True:
    print(f'hora {time.localtime().tm_hour} minuto {time.localtime().tm_min} segundo {time.localtime().tm_sec}')
    time.sleep(1)