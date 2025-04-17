# 🧮 Como calcular a hipotenusa de um triângulo retângulo em Python?
#
# Este programa recebe os comprimentos dos catetos oposto e adjacente
# e calcula a hipotenusa do triângulo retângulo de duas maneiras:
# - Usando a fórmula direta do Teorema de Pitágoras: √(co² + ca²)
# - Usando a função `hypot()` da biblioteca `math`, que faz esse cálculo automaticamente.
# Um ótimo exemplo para aprender conceitos matemáticos e aplicar diferentes abordagens com Python.

# ✅ Método 1: Usando a fórmula diretamente
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}.'.format(hi))

# ✅ Método 2: Usando a função pronta da biblioteca math
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}.'.format(hi))
