def text_to_snake(texto):
    return texto.lower().replace(' ', '_')


def text_to_camel(texto):
    final = texto.title().replace(' ', '')
    return final[0].lower() + final[1:]


def camel_to_snake(texto):
    for letra in texto:
        if letra.isupper():
            texto = texto.replace(letra, f'_{letra.lower()}')
    return texto


def snake_to_camel(texto):
    texto = texto.replace('_', ' ').title().replace(' ', '')
    return texto[0].lower() + texto[1:]


msg = 'texto_em_snake_case'

print(snake_to_camel(msg))
