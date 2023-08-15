# calcule o valaor do produto, a vista (dinheiro/ cheque) 10% desconto, a vista (cartao) 5% desconto, 2x no cartao preço normal, 3x cartao 20% de juros
valProduto = float(input('valor do produto: R$'))
pagamento = str(input('forma de pagamento: '))
dinheiroCheque =  valProduto -(valProduto * 0.10)
cartao = valProduto - (valProduto * 0.05)
juros = valProduto + (valProduto * 0.20)
if pagamento == 'dinheiro' or pagamento == 'cheque':
    print('vc pagou em {} e tem desconto de 10%, novo valor:  R${:.2f}'.format(pagamento, dinheiroCheque))
elif pagamento == 'cartao':
    parcelado = int(input('quantas vezes gostaria de parcelar? '))
    if parcelado == 1:
        print('pagamento no {} , desconto de 5%, novo preço: R${:.2f}'.format(pagamento, cartao))  
    elif parcelado == 2:          
        print('preço normal, R${}'.format(valProduto))    
    elif parcelado >= 3 :
        print('parcelado em {}, juros de 20% , valor: R${}'.format(pagamento, juros))    