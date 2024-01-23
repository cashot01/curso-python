# pa mostrar os 10 primeiros nº
print("="*20)
print('Pa com 10 Termos')
print('='*20)
primeiroTermo = int(input('primeiro termo: '))
razao = int(input('razão: '))
n = int(input('quantos nº vai exibir: '))

ultimo = primeiroTermo + (n-1)*razao
ultimo += 1

for c in range(primeiroTermo, ultimo, razao):
    print(c)
