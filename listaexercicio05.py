'''Faça um algoritmo que receba dois números e ao final mostre a soma, subtração, multiplicação e a divisão dos números lidos.
'''
# Entrada de dados:
R = float(input('Digite um número: '))
T = float(input('Digite outro número: '))
# Processamento:
soma = R + T
subtracao = R - T
multiplicacao = R * T
divisao = R/T
# Saída de dados:
print(f'A soma dos números é: {soma}')
print(f'A subtração dos números é: {subtracao}')
print(f'A multiplicação dos números é: {multiplicacao}')
print(f'A divisão dos números é: {divisao}')