# Este programa solicita um número ao usuário e mostra:
# - O dobro
# - O triplo
# - A raiz quadrada do número

n = int(input('Digite um número: '))
print('O dobro de {} vale {}.\nO triplo de {} vale {}.\nA raiz quadrada de {} vale {:.2f}.'.format(n, (n*2),n, (n*3),n, (n**(1/2))))

