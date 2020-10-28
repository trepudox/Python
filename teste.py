entrada_usuario = input('Digite o CNPJ sem pontos e traços: ')
cnpj_original = entrada_usuario
cnpj_calculo = cnpj_original[:-2]

print(cnpj_original)
print(cnpj_calculo)