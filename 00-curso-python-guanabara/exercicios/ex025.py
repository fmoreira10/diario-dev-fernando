# 🔤 Como analisar e extrair informações de um nome completo?
#
# Este programa pede ao usuário que digite seu nome completo e, em seguida,
# realiza diversas análises usando funções de string em Python:
# - Mostra o nome em letras maiúsculas e minúsculas;
# - Conta quantas letras tem ao todo (ignorando os espaços);
# - Informa o primeiro nome e quantas letras ele possui.
#
# Excelente para praticar o uso de `.strip()`, `.upper()`, `.lower()`, `.split()` e `len()`.

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúscula é {}.'.format (nome.upper()))
print('Seu nome em minúsculo é {}.'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('O primeiro nome é {} e tem {} letras.'.format(separa[0], len(separa[0])))
#print('O primeiro nome é {} e tem {} letras.'.format(separa[0],nome.find(' ')))











