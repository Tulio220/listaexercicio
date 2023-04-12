'''Escrever um algoritmo para determinar o consumo médio de um automóvel sendo fornecida a distância total percorrida pelo automóvel e o total de combustível gasto'''
# Entrada de dados:

dt = float(input('Digite a distancia total percorrida em quilometros: '))
c = float(input('Digite o gasto de combustível: '))

# Processamento:
R = dt/c

# Saída de dados:

print(f'O consumo médio do automóvel em litros por quilometros: {R}')


