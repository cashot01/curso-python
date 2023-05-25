# leia frase , mostre quantas vezes a letra 'a', em que posição aparece na primeira vez, em qu posição aparece na ultima vez
frase = str(input('frase: ')).upper().strip()
          
print('letra A aparece: {} vezes'.format(frase.count('A')))
print('primeira vez no inicio: {}'.format(frase.find('A')+1))