while True:
    print('='*30)
    print('BANCO CEV'.center(30))
    print('='*30)
    sacar = int(input('Que valor você quer sacar? R$'))

    if sacar % 2 == 1:
        print('Não é possível sacar esse valor. O caixa não é possui cédulas de R$1.')
        print('Por favor, digite outro valor.\n')
        continue # Volta ao início do laço
    else:
        total = sacar
        céd = 50
        totcéd = 0
        while True:
            if total >= céd:
                total -= céd
                totcéd += 1
            else:
                if totcéd > 0:
                    print(f'Total de {totcéd} cédulas de R${céd}')
                if céd == 50:
                    céd = 20
                elif céd == 20:
                   céd = 10
                elif céd == 10:
                   céd = 2
                totcéd = 0
                if total == 0:
                    break
        print('='*30)
        print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
        break # finaliza o programa após saque bem-sucedido