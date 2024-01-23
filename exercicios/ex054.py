# 7 anos de nascimento , e mostre quem é maior e menor de idade
from datetime import date
atual = date.today().year # comando usasado para pegar o ano atual
totalMaior = 0
totalMenor = 0
for pessoas in range (1, 8):
    nasceu = int(input('nasceu em qual ano? '))
    idade = atual - nasceu
    if idade >= 21:
        totalMaior += 1
    else:
        totalMenor += 1
print('maiores:  {} pessoas'.format(totalMaior))
print('menores:  {} pessoas'.format(totalMenor))
