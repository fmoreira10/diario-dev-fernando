valor = input('Digite algo: ')

print('o tipo primitivo desse valor é', type(valor))
print('Só tem espaços?', valor.isspace())
print('É um número?', valor.isnumeric())
print('É alfabeto?', valor.isalpha())
print('É alfanumérico', valor.isalnum())
print('Está em maiúsculas?',valor.isupper())
print('Está em minúculas?', valor.islower())
print('Está capitalizado?', valor.istitle())
