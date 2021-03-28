# Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor.

num = int(input('Digite um número: '))
s = num + 1
a = num - 1
print('O número é {}, seu antecessor é {} e o sucessor é {}.'.format(num, a, s))
