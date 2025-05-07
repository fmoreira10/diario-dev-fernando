nome = str(input('Qual o seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('Silva' in nome.title()))

# duas formas de se fazer
nome = str(input('Qual o seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
