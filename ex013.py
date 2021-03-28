# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sal = float(input('Salário: '))
aument = sal + (sal * 0.15)

print('O novo salário, com aumento de 15%, é R$ {:.2f}.'.format(aument))
