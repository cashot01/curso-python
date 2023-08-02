# distancia de viagem em km, calcule o preço 0,50 * km ate 200km, e 0,45 para maior
d = float(input('distancia da viagem: '))
if d <= 200:
    preco = 0.50 * d 
    print('preço: R${:.2f}'.format(preco))
else:
    preco = 0.45 * d
    print('preço: R${:.2f}'.format(preco))    