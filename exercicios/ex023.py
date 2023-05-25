# leia um nº entre 0 a 9999 e mostre a unidade, dezena centena, milhar
numero = int(input('numero: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('unidade: {}'.format(u))
print('desena: {}'.format(d))
print('centana: {}'.format(c))
print('milhar: {}'.format(m))