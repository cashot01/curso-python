# contagem regressiva dos fogos de 10 ate 0, com pausa de 1 segundo
import time
for c in range(10, 0, -1):
    time.sleep(1)
    print(c)
print('feliz ano novo')    