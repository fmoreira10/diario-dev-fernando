# 🧮 Como exibir a tabuada de um número usando Python?
#
# Este programa solicita ao usuário que digite um número inteiro
# e exibe a tabuada desse número de 1 a 10. Além de ser um ótimo
# exercício para iniciantes, também reforça o uso de formatação de strings
# com alinhamento e operadores aritméticos.

num = int(input('Digite um número para ver sua tabuada: '))
print('-'*12)
print(f'{num} x {1:2} = {num*1}')
print('{} x {:2} = {}'.format(num, 2, num*2))
print('{} x {:2} = {}'.format(num, 3, num*3))
print('{} x {:2} = {}'.format(num, 4, num*4))
print('{} x {:2} = {}'.format(num, 5, num*5))
print('{} x {:2} = {}'.format(num, 6, num*6))
print('{} x {:2} = {}'.format(num, 7, num*7))
print('{} x {:2} = {}'.format(num, 8, num*8))
print('{} x {:2} = {}'.format(num, 9, num*9))
print('{} x {:2} = {}'.format(num, 10, num*10))
print('-'*12)
