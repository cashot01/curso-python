# conversão de bases
n = int(input('nº inteiro: '))
print(''' escolha uma das bases para conversão: 
    [1] binario
    [2] octal
    [3] hexadecimal ''')
opcao = int(input('sua opção: '))
if opcao == 1:
    # [2:] serve para fatiar a string começa na terireira posição, pra ficar so com nº 
    print('{} convertido para binario é {}'.format(n, bin(n) [2:]))  #bin transforma em binario
elif opcao == 2:                                      
    print('{} para octal é {}'.format(n, oct(n) [2:]))
elif opcao == 3:
    print('{} para hexadecimal é {}'.format(n, hex(n) [2:]))
elif opcao >= 4:
    print('opção invalida, digite opção entre 1 a 3 ')            
