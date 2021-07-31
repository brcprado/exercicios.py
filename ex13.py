n1 = float(input('Digite seu salário e veja quanto receberá no próximo mês: '))
aum = n1 * 0.15
sal = n1 + aum
print(f'Com 15% de aumento, você passará a receber R${sal:.2f}')

#salário com aumento de 15%. usei uma variável para saber o valor que seria adicionado ao salário
#e depois criei outra, somando os dois (salario antigo + aumento)