# calcule o valaor do produto, a vista (dinheiro/ cheque) 10% desconto, a vista (cartao) 5% desconto, 2x no cartao preço normal, 3x cartao 20% de juros
valProduto = float(input('valor do produto: R$'))
print(''' Formas de pagamento
      [1] dinheiro/cheque
      [2] cartão
      [3] 2x no cartão
      [4] 3x ou mais no cartao ''')
pagamento = int(input('forma de pagamento: '))
dinheiroCheque =  valProduto -(valProduto * 0.10)
cartao = valProduto - (valProduto * 0.05)
juros = valProduto + (valProduto * 0.20)
if pagamento == 1:
    print('vc pagou no dinheiro/cheque  e tem desconto de 10%, novo valor:  R${:.2f}'.forma(dinheiroCheque))
elif pagamento == 2:
        print('pagamento no cartão , desconto de 5%, novo preço: R${:.2f}'.format(cartao)) 
          
elif pagamento == 3:       
    print('preço normal, R${}'.format(valProduto))    
elif pagamento == 4 :
    parcelado = int(input('quantas vezes gostaria de parcelar? '))
    print('parcelado em {}x, juros de 20% , valor: R${}'.format(parcelado, juros))    