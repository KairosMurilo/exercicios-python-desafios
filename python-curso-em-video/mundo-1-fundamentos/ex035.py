#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

a = int(input("Digite o comprimento da 1º reta: "))
b = int(input("Digite o comprimento da 2º reta: "))
c = int(input("Digite o comprimento da 3º reta: "))

if a < b + c and b < a + c and c < a + b:
    print("É possível formar um triangulo com essas retas")
else:
    print("Não é possível formar um triangulo com essas retas")