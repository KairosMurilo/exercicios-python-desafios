#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

ano_atual = date.today().year
cont = 0
for i in range(7):
    ano = int(input(f"Digite o ano de nascimento da {i+1}º pessoa: "))
    if ano_atual - ano > 18:
        cont += 1

print(f"Existem {cont} maiores de idade e {7-cont} menores de idade")