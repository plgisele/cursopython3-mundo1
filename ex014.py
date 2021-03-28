# Escreva um programa que converta uma temperatura digitada em graus Celsius e converta para graus Fahrenheit.

c = float(input('Temperatura em °C: '))
f = ((9 * c) / 5) + 32

print('A temperatura em Fahrenheit é {:.1f}°F'.format(f))
