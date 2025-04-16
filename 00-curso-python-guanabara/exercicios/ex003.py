# Este programa realiza operações matemáticas básicas entre dois números fornecidos pelo usuário.
# Ele solicita dois valores inteiros e, em seguida, calcula:
# - A soma
# - A subtração
# - A multiplicação
# - A divisão (com verificação de divisão por zero)
# A divisão é exibida com duas casas decimais, e se o segundo número for zero, o programa informa que não é possível dividir.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))

s = n1 + n2
sub = n1 - n2
mult = n1 * n2

# Verifica se a divisão é possível antes de realizá-la
if n2 == 0:
    div = "Erro! Divisão por zero não permitida."
else:
    div = f"{n1 / n2:.2f}"  # Formata com duas casas decimais

#print('A soma entre',n1,'e', n2,'vale' , s)
print('A soma entre {} e {} vale {}'.format(n1, n2, s))
print('A subtração vale:', sub)
print('A multiplicação vale:', mult)
print('A divisão vale:', div)  # Exibe a divisão ou mensagem de erro






