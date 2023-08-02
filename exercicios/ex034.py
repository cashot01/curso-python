# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.Para salários superiores a R$1.250,0, calcule um aumento de 10%. Para salários inferiores ou iguais, o aumento é de 15%.

sal = int(input('seu salario: '))
if sal <= 1250:
    aumento = (sal *(0.15)) 
    newSal = aumento + sal
    print('novo salario: {:.2f}'.format(newSal))
else:
    aumento = (sal *(0.10))
    newSal = aumento + sal
    print(newSal)    