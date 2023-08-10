# media das notas, <5 reprovado, entre 5 e 6.9 recuperação, >= 7 passou
nota1 = float(input('nota 1: '))
nota2 = float(input('nota 2: '))
media = (nota1 + nota2)/2
print('media: {}'.format(media))
if media < 5:
    print('REPROVADO, estude mais')
elif media >= 5 and media <= 6.9:
    print('RECUPERAÇÃO')
elif media >= 7:
    print('PARABENS PASSOU')        
