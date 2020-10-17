np1 = float(input('Digite a nota da sua NP1: '))
np2 = float(input('Digite a nota da sua NP2: '))

media_semestral = (2 * np1 + 3 * np2) / 5

if media_semestral >= 7:
    print('Aluno aprovado')
    print('Média final: {:.2f}'.format(media_semestral))
else:
    print('O aluno não foi aprovado e precisará fazer o exame.')
    exame = float(input('Digite a nota do seu exame: '))
    media_final = (media_semestral + exame) / 2
    if media_final >= 5:
        print('Aluno aprovado')
        print('Média final: {:.2f}'.format(media_final))
    else:
        print('Aluno reprovado')
        print('Média final: {:.2f}'.format(media_final))
