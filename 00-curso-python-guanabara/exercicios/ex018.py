# 📐 Como calcular a raiz quadrada de um número inteiro em Python?
#
# Este programa solicita um número inteiro do usuário,
# calcula sua raiz quadrada utilizando a função `sqrt` da biblioteca `math`,
# e exibe o resultado arredondado para baixo com `math.floor`.
# Uma boa prática para aprender importações, uso de bibliotecas externas
# e funções matemáticas nativas do Python.

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num,math.floor(raiz)))
