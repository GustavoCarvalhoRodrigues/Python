# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.

from math import trunc

num = float(input("Digite um número: "))
p_inteira = trunc(num)
print(f'O número {num} tem a porção inteira {p_inteira}')