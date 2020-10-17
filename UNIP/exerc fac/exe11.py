#Escreva um programa que leia números inteiros. O programa deve ler até que o usuário digite 0. No final da execução
#exiba a quantidade de numeros digitados assim como a soma e a media aritmética
x = 1
contador = 0
soma = 0
media = 0

while True:
    if x == 0:
        break

    x = int(input('Digite um número, caso queira encerrar o programa digite 0: '))

    contador += 1
    soma += x

    print(x)



contador -= 1

if contador <= 0:
    print('A quantidade de números digitados foi de: 1\nA soma de todos os números foi de: {}\nA média de todos os '
          'números é de: {:.2f}\nFim do programa.'.format(soma, media))
else:
    media = soma / contador
    print('A quantidade de números digitados foi de: {}\nA soma de todos os números foi de: {}\nA média de todos os '
      'números é de: {:.2f}\nFim do programa.'.format(contador, soma, media))


