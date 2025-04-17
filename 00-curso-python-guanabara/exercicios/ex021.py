# 📐 Como calcular seno, cosseno e tangente de um ângulo em Python?
#
# Este programa solicita um ângulo em graus ao usuário
# e calcula seu seno, cosseno e tangente utilizando a biblioteca `math`.
# Como as funções trigonométricas em Python trabalham com radianos,
# é feita a conversão com `math.radians()` antes dos cálculos.
# Um ótimo exercício para aprender sobre trigonometria e conversão de unidades.

import math
ângulo = float(input('Digite o angulo que você deseja:'))

seno = math.sin(math.radians(ângulo))
cosseno = math.cos(math.radians(ângulo))
tangente = math.tan(math.radians(ângulo))

print('O ângulo de {} tem SENO de {:.2f}'.format(ângulo,seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ângulo, tangente))
