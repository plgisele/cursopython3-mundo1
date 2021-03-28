# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

x = float(input('Digite a distância em metros: '))
cm = x * 100
mm = x * 1000

print('A metragem em centímetro é {:.2f} cm e em milímetro é {:.2f} mm.'.format(cm, mm))
