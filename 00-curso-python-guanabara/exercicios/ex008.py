# Este programa solicita um número ao usuário e mostra:
# - O dobro
# - O triplo
# - A raiz quadrada do número

n = int(input('Digite um número: '))
print(f'O dobro de {n} vale {n*2}.\nO triplo de {n} vale {n*3}.\nA raiz quadrada de {n} vale {(n**(1/2)):.2f}.')
