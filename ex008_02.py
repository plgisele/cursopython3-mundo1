# Escreva um programa que leia um valor em metros e o exiba convertido em quilômetro, hectômetro, decâmetro, decímetro, centímetro e milímetro.

x = float(input('Digite a distância em metros: '))
km = x * 0.001
hm = x * 0.01
dam = x * 0.1
dm = x * 10
cm = x * 100
mm = x * 1000

print('A medida {:.2f}m corresponde a:'.format(x))
print('{:.3f} km'.format(km))
print('{:.2f} hm'.format(hm))
print('{:.1f} dam'.format(dam))
print('{:.0f} dm'.format(dm))
print('{:.0f} cm'.format(cm))
print('{:.0f} mm'.format(mm))
