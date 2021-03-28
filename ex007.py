# Desenvolva um programa que leia duas notas de um aluno, calcule e mostre a sua média.

nota1 = float(input('Nota 01: '))
nota2 = float(input('Nota 02: '))
media = (nota1 + nota2) / 2

print('A média do aluno é {:.1f}.'.format(media))
