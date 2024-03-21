# pedra papel tesousa
import os
os.system("cls")
import random
print(''' JOKENPÔ
      Digite um dos numeros para jogar
      [1] pedra
      [2] papel
      [3] tesoura ''')
maquina = random.randint(1, 3)
myJogada = int(input('sua escolha: '))
if maquina == myJogada:
    print('EMPATE')
if maquina == 1 and myJogada == 3:
    print('PC ganhou, pedra > tesoura ')  
elif maquina == 2 and myJogada == 1:
    print('PARABENS vc GANHOU, papel > pedra')    
elif maquina == 3 and myJogada ==  2:
    print('PC ganhou, tesoura > papel')
elif myJogada == 1 and maquina == 3:
    print('PARABENS vc ganhou, pedra > tesoura ')    
elif myJogada == 2 and maquina == 1:
    print('PARABENS ganhou, papel > pedra')  
elif myJogada == 3 and maquina == 2:
    print('PARABENS vc ganou, tesoura > papel')      
if myJogada > 3:
    print('digite 1, 2, ou 3 para jogar jokempô')    

