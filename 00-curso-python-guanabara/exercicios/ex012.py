# 💸 Quanto dinheiro em reais é necessário para comprar dólares ou euros?
#
# Este programa em Python pede ao usuário o valor em reais disponível na carteira
# e exibe quanto isso equivale em dólares e euros, considerando taxas de câmbio fixas.
# Um ótimo exemplo para praticar entrada de dados, operações matemáticas e
# formatação de números com casas decimais.

real = float(input('Quanto você tem na carteira? R$ '))
dolar = real / 5.78
euro = real / 5.99
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
print('Com R${:.2f} você pode comprar €{:.2f} '.format(real, dolar ))

