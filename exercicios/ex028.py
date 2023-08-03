# computador pensar em numero inteiro de 0 a 5 , e tente acertar

from random import randint
"""n1 = str('0')
n2 = str('1')
n3 = str('2')
n4 = str('3')
n5 = str('4')
n6 = str('5')
lista = [n1, n2, n3, n4, n5, n6]
escolhido = random.choice(lista)"""
escolhido = randint(0, 5) # faz o computador "pensar"
numero = int(input("numero entre 0 e 5: "))
if numero == escolhido:
    print('acertou mizeravi')
else:
    print('errou')  
print('numero escolhido foi: {}'.format(escolhido))    
      