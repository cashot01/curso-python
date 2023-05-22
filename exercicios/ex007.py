# mostra 2 notas , calcule a media
n1 = float(input('nota 1: '))
n2 = float(input('nota 2: '))
media = (n1+n2)/2
print('sua nota 1 {}, sua nota 2 {}, seu media {}'.format(n1, n2, media))
if media < 6:
    print('vc foi reprovado')
else:
    print('vc foi aprovado');

