#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

def soma_dos_quadrados():

    lista = []
    totalizador = 0

    while totalizador < 10:

        lista.append(int(input(f'Entre com {totalizador}º valor:')))
        totalizador += 1

    calculo = sum(lista) ** 2
    print(calculo)

soma_dos_quadrados()


