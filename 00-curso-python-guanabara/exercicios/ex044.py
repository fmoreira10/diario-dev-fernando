print('\033[31mOlá, Mundo!')
print('\033[31;40mOlá, Mundo!')
print('\033[1;31;47mOlá, Mundo!')
print('\033[4;31;43mOlá, Mundo!\033[m')
nome = 'Fernando'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[m',
         'pretoebranco':'\033[7:30m'}

print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome,cores['limpa']))