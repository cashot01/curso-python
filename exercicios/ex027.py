# leia nome completo , primeiro e ultimo nome
nome = str(input('Nome completo: ')).strip()
primeiro = nome.split()
print('primeiro nome: {}'.format(primeiro[0]))
print('ultimo nome: {}'.format(primeiro[len(primeiro)-1]))