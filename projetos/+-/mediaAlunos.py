numero_alunos = int(input('Numero de alunos: '))
numero_notas = int(input('Número de notas: '))
dicionario_aluno = {}
for i in range(numero_alunos):
    print()
    dicionario_aluno[f'Aluno {i+1}'] = []
    for nota in range(numero_notas):
        dicionario_aluno[f'Aluno {i+1}'].append(float(input(f'Aluno {i+1}, nota {nota+1}: ')))

with open('mediaAlunos.txt', 'a+') as file:
    for aluno, notas in dicionario_aluno.items():
        file.write(f'Media {aluno}: {round(sum(notas)/2, 2)}\n')

    file.write('\n')
