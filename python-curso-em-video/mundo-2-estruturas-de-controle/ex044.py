#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal
#– 3x ou mais no cartão: 20% de juros

preco = float(input("Primeiramente, qual o valor do produto? "))
print("Selecione a forma de pagamento: \n"
      "[1] à vista dinheiro/cheque: 10% de desconto \n"
      "[2] à vista no cartão: 5% de desconto\n"
      "[3] em até 2x no cartão: preço formal\n"
      "[4] 3x ou mais no cartão: 20% de juros")
escolha = int(input("Sua opção: "))
if escolha == 1:
    total = preco - (preco - (preco * 0.10))
    print(f"O valor a ser pago será de R${total}")
elif escolha == 2:
    total = preco - (preco - (preco * 0.5))
    print(f"O valor a ser pago será de R${total}")
elif escolha == 3:
    parcela = preco/2
    print(f"O valor a ser pago será de R${preco} em duas parcelas de R${parcela}")
elif escolha == 4:
    total = preco + (preco * 0.20)
    parcela = total / 3
    print(f"O valor a ser pago será de R${total} em três parcelas de R${parcela}")
else:
    print("Opção inválida. Tente novamente")