#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
aux = termo + (10-1) * razao
for i in range(termo, aux, razao):
    print(i)