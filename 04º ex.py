#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

import sys

def consoantes():

    consoantes = ['B','C','D','F','G','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z']
    totalizador = 0
    cliente = []

    while totalizador < 10:

        cliente.append(str.upper(input('Entre com uma letra:')))
        totalizador += 1

    for i in consoantes:
        for j in cliente:
            if (i==j):
                sys.stdout.write(i)

consoantes()

