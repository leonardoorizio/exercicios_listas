#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

def vetor():

    lista = []
    totalizador = 0

    while totalizador < 10:

        totalizador += 1
        lista.append(int(input(f'Digite o {totalizador}º número:')))
        lista.sort(reverse=True)

    print(lista)

vetor()

