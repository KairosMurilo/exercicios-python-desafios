# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input("Digite um número: "))
primo = 0

if num < 2:
    print(f"{num} não é primo")
else:
    primo = 1
    for i in range(2, num):
        if num % i == 0:
            primo = 0

if primo == 0:
    print(f"{num} não é Primo")
else:
    print(f"{num} é Primo")
