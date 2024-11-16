# faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

from math import sqrt

c_oposto = float(input('Digite o comprimento do cateto oposto: '))
c_adjacente = float(input('Digite o comprimento do cateto adjacente: '))

hipotenusa = sqrt(c_oposto**2 + c_adjacente**2)
print(f'Cateto oposto: {c_oposto} e Cateto adjacente: {c_adjacente} e sua Hipotenusa: {hipotenusa:.2f}')