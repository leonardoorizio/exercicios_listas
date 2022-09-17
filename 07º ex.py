# Faça um programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

from math import prod

def vetor():

    numeros_inteiros = []
    totalizador = 1

    while totalizador < 6:

        numeros_inteiros.append(int(input(f'Insira o {totalizador}º número:')))
        totalizador += 1

    soma = sum(numeros_inteiros)
    multiplicacao = prod(numeros_inteiros)

    print(f'\nSoma: {soma}')
    print(f'\nMultiplicação: {multiplicacao}')
    print(f'\nNúmeros informados: {numeros_inteiros}')

vetor()