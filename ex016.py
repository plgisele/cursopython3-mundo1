# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
from math import trunc

num = float(input('Digite um número real: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, trunc(num)))
