# Como calcular o preço de um produto com desconto?
#
# Este programa em Python solicita o preço original de um produto
# e calcula o novo valor com 5% de desconto.
# É uma forma simples e prática de entender porcentagens e formatação de valores.

preço = float(input('Qual é o preço do produto? R$ '))
novo = preço - (preço * 5 / 100)
print(f'O produto que custava R${preço:.2f}, na promoção com desconto de 5% vai custar R${novo:.2f}.')
