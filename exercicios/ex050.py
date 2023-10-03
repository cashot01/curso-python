# 6 nº , se for par soma eles , senao descarta
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('digite o n{}: '.format(c)))
    if num % 2 == 0:
        soma = soma + num  # ou soma += num
        cont += 1
    else:
        print('nº impar, segue o jogo')
print('a soma dos {} nº pares foi: {}'.format(cont, soma))
            