print('-'*30)
print('        LOJA SUPER BARATÃO')
print('-'*30)
total = totmil = menor = cont = 0
barato = ' '
caro = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))
    cont +=1
    total += preço
    if preço > 1000:
        totmil += 1
        caro = produto
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos que é o {caro} e está custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')