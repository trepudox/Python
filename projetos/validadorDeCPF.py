def formula(x, cpf):
    conta = 11 - (x % 11)
    if conta > 9:
        cpf += '0'
        return cpf
    else:
        cpf += str(conta)
        return cpf


entradacpf = input('Digite um cpf, apenas números: ')

saidacpf = entradacpf[0:9]

contador = 10
soma = 0

for num in saidacpf:
    soma += int(num) * contador
    contador -= 1

saidacpf = formula(soma, saidacpf)

contador = 11
soma = 0

for num2 in saidacpf:
    soma += int(num2) * contador
    contador -= 1

saidacpf = formula(soma, saidacpf)

sequencia = entradacpf == entradacpf[0] * len(entradacpf)

if entradacpf == saidacpf and not sequencia:
    print('O CPF {}.{}.{}-{} é válido.'.format(entradacpf[0:3], entradacpf[3:6], entradacpf[6:9], entradacpf[9:]))
else:
    print('O CPF {}.{}.{}-{} é inválido.'.format(entradacpf[0:3], entradacpf[3:6], entradacpf[6:9], entradacpf[9:]))
