dia = int(input('dias: '))
km = float(input('km: '))
total = (dia * 60) + (km * 0.15)
print('total a pagar: R${:.2f}'.format(total))