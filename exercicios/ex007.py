# mostra 2 notas , calcule a media
n1 = float(input('nota 1: '))
n2 = float(input('nota 2: '))
media = (n1+n2)/2
print('sua nota 1 {}, sua nota 2 {}, seu media {}'.format(n1, n2, media))
if media < 6:
    print('\033[0;31mvc foi reprovado\033[m')
else:
    print('\033[1;32mvc foi aprovado\033[m');

