# Como calcular o novo salário de um funcionário com aumento percentual?
#
# Este programa em Python solicita o salário atual de um funcionário
# e calcula o valor com um aumento de 15%.
# Uma aplicação direta de porcentagens e formatação de saída.

salário = float(input('Qual é o salário do Funcionário? R$'))
novo = salário + (salário * 15 / 100)
print('Um funcionário que ganhava R${}, com 15% de aumento, passa a receber R${:.2f}.'.format(salário,novo))
