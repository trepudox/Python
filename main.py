entrada = input()

entrada = entrada[::-1]
res = ''

for char in entrada:
    if char == ' ':
        res += ' '
        continue
    elif not char.isalpha():
        res += ''
    else:
        res += char
else:
    print(res)
