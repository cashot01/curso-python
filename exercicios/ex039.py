# idade , mostre se ainda vai se alistar, ano de alist5amento, ja passou o alistamento, mostrar 
anoAtual = int(input('ano atual: '))
nascimento = int(input('ano de nascimento: '))
idade = anoAtual - nascimento
alistamento = 18
menos18 = alistamento - idade
mais18 = idade - alistamento
print('idade: {} anos'.format(idade))
if idade == 18:
    print('alistamento nesse ano, fique esperto')
elif idade < 18:
    print('seu alistamento acontece em: {} anos'.format(menos18))
elif idade > 18:
    print('alistamento feito há {} anos atras'.format(mais18))    

