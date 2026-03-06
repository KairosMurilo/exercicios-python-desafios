#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valorC = float(input("Digite o valor da casa: "))
salario = float(input("Digite o salário do comprador: "))
anos = int(input("Digite em quantos anos pretende pagar: "))

prestacao = valorC / (anos * 12)
if prestacao > (salario * 0.30):
    print(f"Para pagar uma casa de R${valorC} em {anos}, ")
    print(f"A prestação será de R${prestacao}")
else:
    print(f"Empréstimo negado")
