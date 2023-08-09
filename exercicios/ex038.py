# leia 2 numeros e mostre o 1º é > 2º ou 2º > 1º, ou os 2 são =
n1 = float(input('digite um numero: '))
n2 = float(input('digite um nº: '))
if n1 > n2:
    print('1º numero é maior')
elif n2 > n1:
    print('2º numero maior')
elif n1 == n2:
    print('os 2 numeros são iguais')    