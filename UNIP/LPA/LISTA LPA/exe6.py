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

# Os resultados foram como o esperado, o programa consegue criptografar uma mensagem, guardá-la em um novo arquivo
# texto, criado através do programa, e também consegue descriptografá-la através deste mesmo arquivo .txt. Usamos
# tratamentos de exceções, para que o programa não desse erro em momento algum, até mesmo quando o arquivo texto que
# fora requisitado não estava presnte no mesmo diretório que programa decripto.py. Tiramos prints do funcionamento do
# programa com os dados inseridos no teste de mesa e tudo saiu como os conformes, o programa criptografa de A até Z,
# criptografa números e até símbolos. Usamos todas as ferramentas que nos foram disponibilizadas nas aulas de IPE,
# tanto teoria quanto laboratório, foram aulas muito claras que ocasionaram em um código eficiente e sem erros.
