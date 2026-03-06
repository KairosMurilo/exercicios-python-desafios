# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.


km = float(input("Quantos Km foram percorridos? "))
dias = int(input("Quantos dias o carro foi alugado? "))

preco_dias = dias * 60
preco_km = km * 0.15
total = preco_dias + preco_km

print(f"O preço total a pagar é: R${total:.2f}")