'''Escrever um algoritmo que leia o nome de um aluno e as notas das três provas que ele obteve no semestre. No final informar o nome do aluno e a sua média (aritmética).
'''
# Entrada de dados:
aluno = input('Digite o nome do aluno: ')
# Processamento:
p1 = float(input('Digite sua primeira nota: '))
p2 = float(input('Digite sua segunda nota: '))
p3 = float(input('Digite sua terceira nota: '))
#Saída:
media_aritmetica = (p1 + p2 + p3)/3

R = print(f'A média aritmética do {aluno} é {media_aritmetica}')



