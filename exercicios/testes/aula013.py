'''i = int(input('inicio: '))
fim = int(input('fim: '))
passo = int(input('passo: '))
for c in range(i, fim+1, passo):  
     # range(intervalo é os 2 primeiros , o terceiro é a iteração(nesse exemplo quantos pulos vai dar)) range(0, 10, 2(vai pular de 2 em 2) ) 
     # no 2º nº do range sempre vai ser o anterior, para adicionar basta colocar +1
    print(c)
print('FINALIZOU')   '''
s = 0
for c in range(0, 4):
    n = int(input('digite algum nº: '))
    s = s + n   # ou s += n
print('a soma de todos os nº foi de {}'.format(s))    