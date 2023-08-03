from datetime import date
# leia ano , mostre se é bissexto

ano = int(input('digite um ano: '))
if ano == 0:
    ano = date.today().year
print(ano)
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('ano bissexto')
else:
    print('ano normal')    