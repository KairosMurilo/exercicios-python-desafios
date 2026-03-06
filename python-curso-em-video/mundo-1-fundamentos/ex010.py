#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere US$1.00 = R$3.27

real = float(input("Quantos reais você tem na carteira? "))
dolar = real//3.27
print(f"Você pode comprar {dolar} dólares")