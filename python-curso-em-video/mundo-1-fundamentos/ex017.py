#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot
ca = float(input("Digite o valor do cateto adjacente: "))
co = float(input("Digite o valor do cateto oposto: "))
hipotenusa = hypot(co, ca)
print(f"Valor da hipotenusa é de: {hipotenusa}")
