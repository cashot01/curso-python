# leia nº real e mostre sua parte inteira ex: 1.222 parte inteira 1
import math
n = float(input('digite nº: '))
n_int = math.trunc(n)     # .trunc -> elimina as casas decimais 
print('parte inteira do nº {} é {}'.format(n, n_int))