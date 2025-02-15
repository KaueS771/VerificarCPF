import re

cpf_recebido = input('Digite seu CPF: ')
cpf = re.sub(r'[^0-9]', '', cpf_recebido)  # Remove caracteres não numéricos

# Verifica se todos os dígitos são iguais
cpf_sequencial = cpf == cpf[0] * len(cpf)

if cpf_sequencial:
    print('CPF inválido (todos os dígitos são iguais)')
else:
    nove_digitos = cpf_recebido[:9]
    contador_regressivo_1 = 10


    resultado_digito_1 = 0
    for digito in nove_digitos:
        resultado_digito_1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -=1
    digito_1 = (resultado_digito_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0


    #Descobrindo o valor do segundo digito

    dez_digitos = nove_digitos + str(digito_1)
    contador_regressivo_2 = 11


    resultado_digito_2 = 0
    for digito in dez_digitos:
        resultado_digito_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -=1
    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9  else 0


    cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'

    if cpf_recebido == cpf_gerado:
        print(f'CPF:{cpf_recebido} é válido')
    else:
        print('CPF inválido')


    
