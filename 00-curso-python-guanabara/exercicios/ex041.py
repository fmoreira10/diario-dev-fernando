salário = float(input('Qual é o salário do funcionário? R$'))
if salário <= 1250:
    atual = (salário * 15 / 100) + salário
else:
    atual = (salário * 10 / 100) + salário
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário, atual))

#outra forma de resolver usando cores
salário = float(input('Qual é o salário do funcionário? R$'))
if salário <= 1250:
    atual = (salário * 15 / 100) + salário
else:
    atual = (salário * 10 / 100) + salário

# Códigos de cor ANSI
amarelo = '\033[33m'
verde = '\033[32m'
reset = '\033[0m'

print(f'Quem ganhava {amarelo}R${salário:.2f}{reset} passa a ganhar {verde}R${atual:.2f}{reset} agora.')
