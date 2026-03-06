#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
aux = 0
cont = 0
for i in range (1, 7, 1):
    num = int(input(f"Digite o {i}º número: "))
    if num % 2 == 0:
        aux += num
        cont += 1

print(f"você informou {cont} números PARES e a soma resultou em  {aux}")