# mostre a altura , largura da parede em metros, calcule a area e a quantidade de tinta para pintar a parede , sabendo que cada litro de tinta pinta 2m quadrados
base = int(input('largura: '))
altura = int(input('altura: '))
m2 = base*altura
tinta = m2 / 2
print('parede: {}m quadrados, litros de tintas: {} '.format(m2, tinta))