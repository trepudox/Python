def forca_da_senha(upper, lower, numero, especial):
    if upper >= 2 and lower >= 2 and numero >= 2 and especial >= 2:
        return 'Muito forte'
    elif upper >= 1 and lower >= 1 and numero >= 1 and especial >= 1:
        return 'Forte'
    elif upper >= 1 and lower >= 1 and numero >= 1:
        return 'Média'
    elif upper >= 1 and lower >= 1:
        return 'Fraca'
    else:
        return 'Muito fraca'


def validacao(senha_usuario):
    char_upper, char_lower, char_especial, char_numero = 0, 0, 0, 0
    caracteres_especiais = ('!', '@', '#', '$', '%', '&', '*')
    if len(senha_usuario) < 7 or ' ' in senha_usuario:
        print('Sua senha precisa ter 7 ou mais caracteres e não pode conter espaço.')
        return

    for char in senha_usuario:
        if char.isupper():
            char_upper += 1
        elif char.islower():
            char_lower += 1
        elif char.isalnum():
            char_numero += 1
        elif char in caracteres_especiais:
            char_especial += 1

    forca = forca_da_senha(char_upper, char_lower, char_numero, char_especial)

    return f'Força da senha: {forca}'


print(validacao(input('Digite sua senha: ')))
