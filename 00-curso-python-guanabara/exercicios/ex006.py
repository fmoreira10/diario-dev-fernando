# Este programa realiza diversas operações matemáticas entre dois números fornecidos pelo usuário:
# soma, subtração, multiplicação, divisão, exponenciação e o resto da divisão (módulo).

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
e = n1 ** n2
r = n1 % n2

print('A soma é: {}\nA subtração é: {}\nA multiplicação é: {}\nA divisão é: {:.2f}\nA exponenciação é: {}\nO resto da divisão é: {}'.format(s, sub, m, d, e, r))

