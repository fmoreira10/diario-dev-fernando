# Este programa pede ao usuário que digite algum valor e, em seguida,
# mostra várias informações sobre esse valor, utilizando métodos de string.
# Ele identifica o tipo primitivo do dado e verifica se ele possui apenas espaços,
# se é numérico, se contém apenas letras, se é alfanumérico, se está em maiúsculas,
# minúsculas ou capitalizado.

valor = input('Digite algo: ')

print('o tipo primitivo desse valor é', type(valor))
print('Só tem espaços?', valor.isspace())
print('É um número?', valor.isnumeric())
print('É alfabeto?', valor.isalpha())
print('É alfanumérico', valor.isalnum())
print('Está em maiúsculas?',valor.isupper())
print('Está em minúculas?', valor.islower())
print('Está capitalizado?', valor.istitle())
