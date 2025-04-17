# Como calcular o preço de um produto com desconto?
#
# Este programa em Python solicita o preço original de um produto
# e calcula o novo valor com 5% de desconto.
# É uma forma simples e prática de entender porcentagens e formatação de valores.

preço = float(input('Qual é o preço do produto? R$ '))
novo = preço - (preço * 5/100)
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}.'.format(preço,novo))
