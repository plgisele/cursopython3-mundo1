# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

ang = float(input('Digite o ângulo desejado: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))

print('Ângulo: {}'.format(ang))
print('Seno: {:.2f}'.format(sen))
print('Cosseno {:.2f}'.format(cos))
print('Tangente: {:.2f}'.format(tg))