import random
dicionario_aluno = {}
for i in range(int(input('Numero de alunos: '))):
    dicionario_aluno[f'Aluno {i+1}'] = []
    for nota in range('Número de notas: '):
        dicionario_aluno[f'Aluno {i+1}'].append(random.randint(0, 10))

with open('arquivo.txt', 'a+') as file:
    for aluno, notas in dicionario_aluno.items():
        file.write(f'Media {aluno}: {sum(notas)/2}\n')
