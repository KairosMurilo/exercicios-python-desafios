#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
#se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

print("[SISTEMA DE ALISTAMENTO]")
ano = int(input("Qual seu ano de nascimento: "))
idade = date.today().year-ano

if idade > 18:
    print(f"Você passou do prazo de alistamento, devia ter se alistado há {idade-18} anos")
elif idade == 18:
    print("Você está na idade exata para o alistamento militar")
else:
    print(f"Você ainda não tem idade o suficiente para o alistamento militar, ainda faltam {18-idade} anos")