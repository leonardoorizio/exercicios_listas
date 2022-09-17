#Faça um programa que peça idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima
# na ordem inversa lida.

def idade_e_altura():

    idade = []
    altura = []

    for i in range(5):

        idade.append(int(input('Entre com a idade:')))
        altura.append(float(input('Entre com a altura:')))

    idade.reverse()
    altura.reverse()

    print(f'Idade: {idade}')
    print(f'Altura: {altura}')

idade_e_altura()