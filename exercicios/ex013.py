# salario, 15% de aumento
salario = float(input('salario:'))
aumento = float(salario * 0.15)
newSalario = salario + aumento
print('salario: R${}, promoção de: 15%  novo salario: R${}'.format(salario, newSalario))