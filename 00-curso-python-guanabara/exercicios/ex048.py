
# Primeira forma de resolver
from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}.')

#Segunda forma de resolver
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1  # acumulador do fatorial
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')
