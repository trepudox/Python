# Asp67a

def do_formato(string: str):
    if len(string) != 6:
        return False

    if not string[0:4].istitle() or string[5].isupper():
        return False

    if not string[0:3].isalpha():
        return False

    if not string[3:5].isdigit():
        return False

    if not string[-1].isalpha():
        return False

    return True


if __name__ == '__main__':
    teste = 'Gas21f'
    print(do_formato(teste))
