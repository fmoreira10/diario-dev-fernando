
# Este programa solicita ao usuário que digite seu nome e sua idade.
# Em seguida, ele exibe uma mensagem personalizada usando as informações fornecidas.
# A função input() é usada para capturar dados do usuário,
# enquanto a função format() insere essas informações dentro da string final.

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
print('É um prazer te conhecer!, {}  {}' .format(nome,idade))
