# 🔀 Como sortear aleatoriamente a ordem de apresentação dos alunos?
#
# Este programa pede o nome de quatro alunos e, em seguida, sorteia
# uma ordem aleatória de apresentação usando a função `shuffle()`
# da biblioteca `random`. Um exemplo simples e divertido de como manipular
# listas e gerar resultados diferentes a cada execução.

from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será ')
print(lista)
