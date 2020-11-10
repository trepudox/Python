# MEIO FUNCIONAL, CUIDADO POIS PODE TRAVAR SEU MOUSE KKKK
import pyautogui
import time


def print_posicao():
    while True:
        try:
            funcx, funcy = pyautogui.position()
            posicao = 'X: ' + str(funcx).rjust(4) + ' | ' + 'Y: ' + str(funcy).rjust(4)
            print(posicao, end='')
            print('\b' * len(posicao), end='', flush=True)
        except KeyboardInterrupt:
            print('\n')
            return


try:
    print('Ctrl-C para sair.')
    print('Posição do mouse:')
    print_posicao()
    try:
        x = int(input('Valor de X: '))
        y = int(input('Valor de Y: '))
        while True:
            # pyautogui.position(x, y)
            pyautogui.moveTo(x, y)
            pyautogui.click()
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass
except KeyboardInterrupt:
    pass
