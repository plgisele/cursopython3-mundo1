# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

cat1 = float(input('Cateto oposto: '))
cat2 = float(input('Cateto adjacente: '))
hipo = hypot(cat1, cat2)

print('A hipotenusa do triângulo com cateto {} e {} é {:.2f}.'.format(cat1, cat2, hipo))