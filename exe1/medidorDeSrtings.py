palv = input('Digite alguma string: ')

if palv.isascii():
    if 0 < palv.__len__() <= 4:
        print('Essa string é curta.')
    elif 5 <= palv.__len__() <= 8:
        print('Essa string é média.')
    elif 9 <= palv.__len__():
        print('Essa string é grande.')
else:
    print('Digite algo por favor.')
