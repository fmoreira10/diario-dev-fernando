# 💡 Qual é a média das notas de um aluno?
# 
# Este programa simples em Python solicita duas notas do usuário,
# calcula a média entre elas e exibe o resultado formatado com uma casa decimal.
# É uma ótima forma de praticar entrada de dados, operações aritméticas
# e formatação de strings com o método format().

n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
print('A media entre {} e {} é igual a {:.1f}.'.format(n1, n2, (n1+n2)/2))

