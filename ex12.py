preço = int(input('Digite o valor do seu produto e veja com o desconto: '))
desc = preço - (preço * 5 / 100)
print(f'O seu produto produto de R${preço} passará a valer {desc} ')
print('você ganhou R$', preço * 5 / 100,' de desconto' )


#cálculo de 5% de desconto (basta  multiplicar o valor original pelo 100 - 5(desconto) = 90 ou em %0.95)#