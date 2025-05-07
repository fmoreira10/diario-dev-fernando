cont = soma = 0
maior = menor = None
continuar = 'S'  # variável de controle

while continuar == 'S':
    try:
        núm = int(input('Digite um número: '))
    except ValueError:
        print('Por favor, digite um número válido.')
        continue

    soma += núm
    cont += 1

    if maior is None or núm > maior:
        maior = núm
    if menor is None or núm < menor:
        menor = núm

    continuar = ''
    while continuar not in ('S', 'N'):
        continuar = input('Quer continuar? [S/N] ').strip().upper()
        if continuar not in ('S', 'N'):
            print('Resposta inválida. Digite apenas S ou N.')

media = soma / cont
print(f'\nVocê digitou {cont} números. A soma foi {soma} e a média é {media:.1f}.')
print(f'O maior valor foi {maior} e o menor foi {menor}.')

