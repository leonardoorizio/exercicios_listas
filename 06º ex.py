#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
#imprima o número de alunos com média maior ou igual a 7.0

def media_estacio():

    totalizador1 = 0
    total_media = []
    maior_que_7 = 0

    while totalizador1 < 2:

        totalizador1 += 1
        notas = []
        totalizador = 1

        while totalizador < 5:

            notas.append(int(input(f'Digite a {totalizador}º nota:')))
            totalizador += 1
            total_media.append(round(sum(notas) / 4))

    for i in total_media:
        if i >= 7:
            maior_que_7 += 1

    print(f'\nNúmero de alunos com média maior que 7º: {maior_que_7}')

media_estacio()
