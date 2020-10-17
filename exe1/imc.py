nome = 'Marco'
idade = 17
peso = 58
altura = 1.65
imc = peso / altura ** 2

print(nome, 'tem', idade, 'anos de idade, tem', peso, 'kg e', altura, 'de altura. Seu imc é igual a', format(imc, '.2f'))
#ou
print(f'\n{nome} tem {idade} anos de idade, tem {peso} kg e {altura} de altura. Seu imc é igual a {imc:.2f}')
#ou
print('\n{} tem {} anos de idade, tem {} kg e {} de altura. Seu imc é igual a {}'.format(nome, idade, peso, altura, format(imc, '.2f')))

'''
imc exercicio:

nome = 'Marco'
idade = 17
altura = 1.65
peso = 58
anoNascimento = 2020 - idade
imc = peso / altura ** 2

print('{0} tem {1} anos, {2} de altura e {3} kg. \nSeu imc é {4}. \n{0} nasceu em {6} ou {5}.'
      .format(nome, idade, altura, peso, format(imc, '.2f'), anoNascimento, anoNascimento - 1))
'''