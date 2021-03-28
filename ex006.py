# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num = int(input('Digite um número: '))
dob = num * 2
tri = num * 3
raiz = num ** (1/2)

print('O número é {}, o dobro do número é {}, o triplo é {} e sua raiz quadrada é {:.2f}.'.format(num, dob, tri, raiz))