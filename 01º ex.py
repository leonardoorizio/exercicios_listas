#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

def vetor():

    lista = []
    totalizador = 0

    while totalizador < 5:

        lista.append(int(input('Entre com número:')))
        totalizador += 1

    print(lista)

vetor()