# mostre nome em maiusculo, minusculo, quantas letras tem(sem espaço), quantas letras primeiro nome

nome = str(input('Qual é seu nome: '))
print(nome)
maiusculo = nome.upper()
print('maiusculo: {}'.format(maiusculo))
minusculo = nome.lower()
print('minusculo: {}'.format(minusculo))
letras_espaco = len(nome) - nome.count(' ')
print('nome tem: {}'.format(letras_espaco))
separa = nome.split()
print('primeiro nome: {} e tem {} letras'.format(separa[0], len(separa[0])))
print('nome trocado: {}'.format(nome.replace('passos', 'topzera')))