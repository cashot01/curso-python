import math #importou a biblioteca matematica
n = int(input('digite um numero: '))
raiz = math.sqrt(n)
print('a raiz de {} é = {}'.format(n, math.ceil(raiz)))

# math.ceil -> arredonda pra cima o numero
# "   .floor -> arredonda pra baixo
# "   .sqrt -> raiz quadrada 
