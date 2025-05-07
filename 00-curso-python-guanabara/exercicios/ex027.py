cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')


cid = str(input('Em que cidade você nasceu? '))

if 'santo' in cid.lower():
    print('Verdadeiro')
else:
    print('Falso')
