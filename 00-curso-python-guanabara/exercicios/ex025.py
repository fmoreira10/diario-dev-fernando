nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúscula é {}.'.format (nome.upper()))
print('Seu nome em minúsculo é {}.'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('O primeiro nome é {} e tem {} letras.'.format(separa[0], len(separa[0])))
#print('O primeiro nome é {} e tem {} letras.'.format(separa[0],nome.find(' ')))











