# pergunta valor da casa , salario e quantos anos vai pagar, calcule a prestação mensal, sabendo que nao pode passar de 30% do salario
casa = float(input('valor da casa: '))
salario = float(input('salario: '))
sal_030 = salario * 0.30 
anos = float(input('anos a pagar:  '))
prestacao = (casa / anos )
print('valor da prestação: {:.2f}'.format(prestacao))
if prestacao <= sal_030:
    print('(R${:.2f}) <=  {:.2f} , emprestimo ACEITO '.format(prestacao, sal_030))
elif prestacao > sal_030:
    print('R${:.2f} > R${:.2f} , emprestimo NEGADO'.format(prestacao, sal_030))    