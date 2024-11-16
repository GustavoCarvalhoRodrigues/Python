# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = int(input('Digite um ângulo qualquer: '))

angulo_rad = math.radians(angulo)

seno = math.sin(angulo_rad)
coss = math.cos(angulo_rad)
tang = math.tan(angulo_rad)

print(f'Ângulo: {angulo}°')
print(f'Ângulo em radianos: {angulo_rad:.4f}')
print(f'Seno: {seno:.4f}')
print(f'Cosseno: {coss:.4f}')
print(f'Tangente: {tang:.4f}')

