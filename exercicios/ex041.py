# mostre idade, atleta ate 9 mirim, 14 infantil, 19 junior, 20 senior, >20 master
anoAtual = int(input('ano atual: ')) 
nascimento = int(input('ano nascimento: '))
idade = anoAtual - nascimento
print('idade: {} anos'.format(idade))
if 0 < idade <= 9:
    print('nadador MIRIM')
elif 9 < idade <= 14:
    print('nadador INFANTIL')    
elif  14 < idade <= 19:
    print('nadador JUNIOR') 
elif idade == 20:
    print('nadador SENIOR')       
elif idade > 20:
    print('nadador MASTER')  
elif idade <= 0:
    print('nadador não existe')      