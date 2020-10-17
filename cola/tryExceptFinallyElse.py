'''

try: - vai tentar executar o bloco de código, caso não consiga ele pula para o except
except: - se algum erro ocorrer (e só se ocorrer), ele executa o bloco de código acoplado a ele
finally: - o bloco de código do finally executa independetemente do que acontecer
else: - o else pode ser usado depois do except, caso nenhum erro ocorra, seu bloco de código será executado

O except precisa receber o tipo de erro que ele vai "ignorar", como por exemplo:

except ValueError:
    print('Erro')

Para receber mais de um erro, ele precisa ser apresentado com parênteses:

except (ValuerError, ZeroDivisionError)
    print('Erro')

TIPOS COMUNS DE EXCEPTION

ImportError: falha ao importar
IndexError: índice fora do range
NameError: uma variável desconhecida é usada
SyntaxError: código ilegível pela máquina
TypeError: uma função é chamada para um valor de tipo inapropriado
ValueError: uma função é chamada com um valor de TIPO correto, mas com o valor inapropriado

'''

# uso de try e except para converter de string para int:

while True:
    try:
        idade = int(input('Qual sua idade? '))
    except ValueError:
        print('Digite apenas números inteiros.')
    else:
        break


print('Fim')
