'''Um motorista deseja colocar no seu tanque X reais de gasolina. Escreva um algoritmo para ler o preço do litro da gasolina e o valor do pagamento, e exibir quantos litros ele conseguiu colocar no tanque.
'''
# Entrada:
gasolina = float(input('Digite a quantidade de gasolina foi colocada: '))

litros = float(input('Digite o preço do litro: '))
# Processamento:
resultado = gasolina/litros
#Saída:
print(f'O tanque foi abastecido com {resultado} litros')
