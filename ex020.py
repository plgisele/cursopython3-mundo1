# O mesmo professor do ex019 quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

nome1 = input('Primeiro aluno: ')
nome2 = input('Segundo aluno: ')
nome3 = input('Terceiro aluno: ')
nome4 = input('Quarto aluno: ')
lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)

print('A ordem de apresentação é: ')
print(lista)
