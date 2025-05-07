while True:
    n = int(input('Quer ver a tabuada de qual número? '))
    print('-' * 35)
    if n < 0:
        break

    i = 1
    while i <= 10:
        print(f'{n} x {i} = {n * i}')
        i += 1
    print('-' * 35)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
