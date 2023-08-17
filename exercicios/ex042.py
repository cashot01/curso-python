# 3 retas formam trinagulo e mostre se são equilatero, isoceles escaleno
r1 = float(input('reta 1: '))
r2 = float(input('reta 2: '))
r3 = float(input('reta 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 +r2:
    print('forma um triangulo')    
elif r1 > r2 + r3 and r2 > r1 + r3 and r3 > r1 +r2:
    print('nao forma triangulo')
if r1 == r2 and r1 == r3 and r2 == r3:   
    print('triangulo equilatero')
elif r1 == r2 or r1 == r3 or r2 == r3:
    print('triangulo isoceles') 
elif r1 != r2 and r1 != r3 and r2!= r3:
    print('triangulo escaleno')     