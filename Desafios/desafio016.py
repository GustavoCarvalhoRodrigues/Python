# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.

from math import trunc

num = float(input("Digite um valor: "))
print(f'O número {num} tem a porção inteira {trunc(num)}')

# num = float(input("Digite um valor: "))
#print(f'O número {num} tem a porção inteira {int(num)}')