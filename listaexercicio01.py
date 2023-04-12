'''A velocidade média de um veículo é dado pela expressão Vm= ∆S/∆t, onde: 
∆S: variação de espaço (ponto de chegada – ponto de partida) em quilômetros
∆t: variação de tempo (tempo final – tempo inicial) em horas
Escreva um programa para calcular a velocidade média dada a variação espacial e a variação temporal.  '''

# Recebe a variação de espaço e tempo do usuário
deltaS = float(input('Digite quantos quilometros você andou: '))
deltaT = float(input('Digite quanto tempo você gastou em horas: '))

# Calcula a velocidade média
velocidade_media = deltaS/deltaT

# Imprime o resultado
print("A velocidade média do veículo é", velocidade_media, "km/h.")
