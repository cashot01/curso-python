# pa mostrar os 10 primeiros nº
print("="*20)
print('Pa com 10 Termos')
print('='*20)
primeiroTermo = int(input('primeiro termo: '))
razao = int(input('razão: '))
decimo = primeiroTermo + (10 - 1)*razao # calculo do decimo termo da pa


for c in range(primeiroTermo, decimo, razao):
    print(c)
