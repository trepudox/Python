'''
ainda falta fazer calculos com numero negativo
'''

print('Calculadora. Para sair faça uma divisão por \'0\'')
num1 = 0
num2 = 0
opr = 0

while opr != '/' or num2 != 0:
    num1 = input('Digite um número: ')
    opr = input('Digite o operador: ')
    num2 = input('Digite outro número: ')

    if not (num1.isnumeric() or num2.isnumeric()):
        print('\nPor favor digite números válidos.\n')
        continue

    else:
        num1 = float(num1)
        num2 = float(num2)

        if num2 == 0 and opr == '/':
            print('\nVocê saiu do programa com êxito.')
            break
        elif opr == '+':
            print(num1 + num2)
        elif opr == '-':
            print(num1 - num2)
        elif opr == '*':
            print(num1 * num2)
        elif opr == '/':
            print(num1 / num2)
        else:
            print('\nPor favor digite um operador válido\n')