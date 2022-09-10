#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
#Imprima os três vetores.

def vetor():

    consolidado = []
    par = []
    impar = []
    totalizador = 0

    while totalizador < 20:

        totalizador += 1
        consolidado.append(int(input(f'Digite o {totalizador}º número:')))

        for i in consolidado:

            if ( i  %  2 ) ==  0:
                if i not in par:
                    par.append(i)
            else:
                if i not in impar:
                    impar.append(i)

    print(f'\nConsolidado: {consolidado}')
    print(f'\nNúmero Par: {par}')
    print(f'\nNúmero Impar: {impar}')

vetor()

