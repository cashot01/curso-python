# mostre peso e altura , calcule o imc, <18.5 abaixo do peso, entre 18.5 e 25 peso ideal, 25 ate 30 sobrepeso, 30 ate 40 obesidade, >40 obesidade morbida
altura = float(input('altura: '))
peso = float(input('peso: '))
imc = peso / (altura ** 2)
print('imc: {:.2f}'.format(imc))
if imc < 18.5:
    print('abaixo do peso')
elif 18.5 < imc < 25:
    print('peso ideal')    
elif 25 < imc < 30:
    print('sobrepeso')
elif 30 < imc < 40:
    print('obesidade')
elif imc > 40:
    print('obesidade morbida')        