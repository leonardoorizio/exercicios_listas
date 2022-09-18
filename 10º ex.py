#Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos
#intercalados dos dois outros vetores.

def vetores_intercalados():

    lista1 = []
    lista2 = []
    lista3 = []

    print('Primeiro Vetor')

    for i in range(10):

        lista1.append(input(f'Digite o valor do {i+1}° caracter: '))

    print('\nSegundo Vetor')

    for i in range(10):

        lista2.append(input(f'Digite o valor do {i+1}° caracter: '))

    for i in range(10):

        lista3.append(lista1[i])
        lista3.append(lista2[i])

    print(f'\nTerceiro vetor: {lista3}')

vetores_intercalados()

