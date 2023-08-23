# soma dos nº impares multiplos de 3, no intervalo de 1 a 500
soma = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 != 0:
        print(c)
        soma = soma + c
print('soma dos nº impares multiplos de 3 = {}'.format(soma))        

        