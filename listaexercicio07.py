'''Ler dois valores para as variáveis A e B, e efetuar as trocas dos valores de forma que a variável A passe a possuir o valor da variável B e a variável B passe a possuir o valor da variável A. Apresentar os valores trocados. Ex: Início A vale 3 e B vale 5 no final da execução A valerá 5 e B valerá 3.
'''
#Entrada de dados:
A = input('Digite o valor de A: ')
B = input('Digite o valor de B: ')
print('-'*50)
print('Valores originais: ')

print(f'{A}')
print(f'{B}')
#Processamento:
print('-'*50)

print('Com as trocas:')

print('-'*50)

A1 = B 
A2 = A
#Saída:
print(f'Valor atual de A é igual a {A1}')
print(f'Valor atual de B é igual a {A2}')

print('-'*50)
