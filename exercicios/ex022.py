# mostre nome em maiusculo, minusculo, quantas letras tem(sem espaço), quantas letras primeiro nome

nome = str(input('Qual é seu nome: '))
print(nome)
maiusculo = nome.upper()
print('maiusculo: {}'.format(maiusculo))
minusculo = nome.lower()
print('minusculo: {}'.format(minusculo))
letras_nome = (nome.join(''))
print('letras sem espaço: {}'.format(letras_nome))