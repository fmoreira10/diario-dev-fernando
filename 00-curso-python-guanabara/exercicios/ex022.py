# 📅 Quantos dias, horas e minutos você já viveu?
#
# Este programa pede a idade do usuário em anos e calcula aproximadamente
# quantos dias, horas e minutos essa pessoa já viveu até agora.
# Um ótimo exercício para praticar operações matemáticas com valores
# e mostrar um resultado interessante no final!

idade = int(input('Digite sua idade em anos: '))

dias = idade * 365
horas = dias * 24
minutos = horas * 60

print('Você já viveu aproximadamente:')
print(f'- {dias} dias')
print(f'- {horas} horas')
print(f'- {minutos} minutos')
