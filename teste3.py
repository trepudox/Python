import time

while True:
    if time.localtime().tm_sec % 2 == 0:
        print(f'segundo {time.localtime().tm_sec} par')
        time.sleep(1)
    else:
        print(f'segundo {time.localtime().tm_sec} impar')
        time.sleep(1)
