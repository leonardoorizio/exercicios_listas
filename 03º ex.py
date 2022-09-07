#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

def notas():

    notas_estacio = []
    provas = int(input('Número de provas aplicadas:'))
    totalizador = 0

    while totalizador < provas:

        totalizador += 1
        notas_estacio.append(float(input(f'{totalizador}º nota:')))

    media = sum(notas_estacio) / provas
    print(f'\nMédia:{media}')

notas()



