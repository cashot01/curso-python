# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.Para salários superiores a R$1.250,0, calcule um aumento de 10%. Para salários inferiores ou iguais, o aumento é de 15%.

sal = int(input('seu salario: '))
if sal <= 1250:
    aumento = (sal *(0.15)) + sal
    print('novo salario: R${:.2f}'.format(aumento))
else:
    aumento = (sal *(0.10)) + sal
    print('novo salario: R${:.2f}'.format(aumento))    