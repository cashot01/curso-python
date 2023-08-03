# radar com multa > 80km/h multa de R$7,00
v = int(input('velocidade: '))
multa = (v-80)*7
if v > 80:
    print('vc foi multado, vai custar R${:.2f}'.format(multa))
else:
    print('velocidade aceita')    
