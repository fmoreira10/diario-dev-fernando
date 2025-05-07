# 🚗 Quanto custa alugar um carro por alguns dias e quilômetros rodados?
#
# Este programa em Python solicita ao usuário a quantidade de dias que um carro foi alugado
# e a distância percorrida em quilômetros. Em seguida, calcula o valor total a pagar,
# considerando R$60 por dia e R$0,15 por km rodado.
# Um exercício útil para praticar entrada de dados, operadores e formatação de valores monetários.

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
total = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(total))
