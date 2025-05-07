# 🔢 Como obter a parte inteira de um número decimal em Python?
#
# Este programa recebe três números decimais inseridos pelo usuário
# e utiliza a função `trunc()` da biblioteca `math` para mostrar apenas a parte inteira de cada número.
# Um ótimo exercício para compreender manipulação de números reais e funções matemáticas em Python.

import math
num = float(input('Digite o primeiro um número: '))
print('O número digitado foi {} tem a parte inteira {}.'.format(num, math.trunc(num)))

from math import trunc
segnum = float(input('Digite o segundo número: '))
print('O segundo número digitado foi {} tem a parte inteira {}.'.format(segnum, trunc(segnum)))

ternum = float(input('Digite o terceiro número: '))
print('O terceiro número digitado foi {} e sua parte inteira é {}.'.format(ternum, int(ternum)))
