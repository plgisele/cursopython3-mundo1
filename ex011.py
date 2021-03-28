# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la.
# Considere que cada litro de tinta pinta uma parea de 2m².

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
a = larg * alt
lit = a / 2

print('A área da parede é {:.2f}m² e é necessário {:.2f}L de tinta para pintá-la.'.format(a, lit))