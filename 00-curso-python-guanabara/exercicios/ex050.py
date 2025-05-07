print('Gerador de PA')
print('-=' * 10)

# Entrada de dados
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

# Variáveis de controle
termo = primeiro
cont = 1
total = 0
mais = 10  # Começa mostrando 10 termos

while mais != 0:
    total += mais  # Atualiza o total de termos desejado
    while cont <= total:
        print(f'{termo} - ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você ainda quer mostrar? '))

print(f'Progressão finalizada com {total} termos mostrados.')
print('FIM')
