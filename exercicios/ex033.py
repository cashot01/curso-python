# 3 numeros e mostre o maior e o menor
n1 = int(input('n1: '))
n2 = int(input('n2: '))
n3 = int(input('n3: '))
#verificando o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3 
print('menor nº: {}'.format(menor))    
# verificando o maior
maior = n1
if n2 > n1 and n2 > n3 :
    maior = n2
if n3 > n1 and   n3 > n2:
    maior = n3 
print('maior nº: {}'.format(maior)) 
diferenca = maior - menor
print('a diferença entre o maior {} e o menor {} é = {}'.format(maior, menor, diferenca))   
