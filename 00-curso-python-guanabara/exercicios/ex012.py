real = float(input('Quanto você tem na carteira? R$ '))
dolar = real / 5.78
euro = real / 5.99
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
print('Com R${:.2f} você pode comprar €{:.2f} '.format(real, dolar ))

