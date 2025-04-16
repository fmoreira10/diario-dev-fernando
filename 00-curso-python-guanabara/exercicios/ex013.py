largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
tinta = area / 2
print('Sua parede tem dimensão de {}x{} e sua área é de {}m2.'.format(largura,altura,area))
print('Para pintar essa parede, você precisará de {}l de tinta'.format(tinta))
