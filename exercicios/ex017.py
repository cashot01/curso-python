# triangulo retangulo moste o cateto oposto e adjacente, calcule a hipotenusa

#import math
from math import hypot
co = float(input('medida do cateto opsto: '))
ca = float(input('medida do cateto adjacente: '))
hipo = hypot(co, ca)
#hipo = math.sqrt((co**2) + (ca**2))
print('hipotenusa mede: {:.2f}'.format(hipo)) 

# math.hypot -> calculo da hipotenusa