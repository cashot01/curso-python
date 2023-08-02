"""nome = str(input('nome: '))
if nome == 'cauan':
    print('nome lindo vc tem')
else:
    print('nome normal')
print('bom dia {}'.format(nome)) """

n1 = float(input('nota 1: '))
n2 = float(input('nota 2: '))
m = (n1 + n2)/2
print('sua media: {:.1f}'.format(m))
if m >= 6:
    print('voce passou')
else:
    print('nao foi desta vez')