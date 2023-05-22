# mostra o preço do produto e mostre com 5% de desconto
valor = float(input('valor do produto: '))
desconto = float(0.05)
novoValor = valor - (valor*desconto)
print('valor do produto: R${}, \n desconto de: {}, \n novo valor: R${}'.format(valor, desconto, novoValor))