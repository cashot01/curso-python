# mostre o angulo , calcule seno cosseno tangente
import math
n = float(input('angulo: '))
sen = math.sin(math.radians(n)) 
cos = math.cos(math.radians(n))
tan = math.tan(math.radians(n))
print(n)
print('Seno de {}º é  {:.2f}'.format(n, sen))
print('Cosseno de {}º é {:.2f}'.format(n, cos))
print('Tangente de {}º é {:.2f}'.format(n, tan))

# .sin -> calcula o seno em radianos
# .cos -> cosseno em radianos
# .tan -> tangente em radianos
# .radians -> trasnforma em radianos