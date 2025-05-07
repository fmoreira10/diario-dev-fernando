# 🎨 Quantos litros de tinta são necessários para pintar uma parede?
#
# Este programa em Python solicita a largura e a altura de uma parede,
# calcula sua área e informa quantos litros de tinta serão necessários para pintá-la.
# Considera-se que 1 litro de tinta cobre 2 metros quadrados de parede.
# Excelente para treinar entrada de dados, cálculo de área e lógica simples.

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
tinta = area / 2
print(f'Sua parede tem dimensão de {largura}x{altura} e sua área é de {area} m².')
print(f'Para pintar essa parede, você precisará de {tinta} litros de tinta.')
