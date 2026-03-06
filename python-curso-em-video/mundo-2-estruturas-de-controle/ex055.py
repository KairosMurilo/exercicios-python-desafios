#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0

for i in range(5):
    peso = float(input(f"Digite o peso da {i+1}º pessoa: "))
    if i == 0:
        maior = peso
        menor = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso

print(f"O maior peso é de {maior} e o menor peso é de {menor}")