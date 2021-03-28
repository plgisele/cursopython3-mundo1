# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considerar US$ 1,00 = R$ 5,50

x = float(input('Quanto dinheiro você tem: '))
dol = x / 5.50
print('Com R$ {} você pode comprar US$ {:.2f}.'.format(x, dol))
