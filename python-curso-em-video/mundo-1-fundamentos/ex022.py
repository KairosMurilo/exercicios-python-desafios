#Crie um programa que leia o nome completo de uma pessoa e mostre:
#   O nome com todas as letras maiúsculas e minúsculas.
#   Quantas letras ao todo (sem considerar espaços).
#   Quantas letras tem o primeiro nome.

nome = str(input("Digite o seu nome completo: ")).strip()
print(f"Maiúsculo: {nome.upper()}")
print(f"Minúsculo: {nome.lower()}")
print(f"Seu nome tem: {len(nome) - nome.count(" ")} letras")
#print(f"Seu primeiro nome tem: {nome.find(" ")} letras")
separa = nome.split()
print(f"Seu primeiro nome é {separa[0]} e tem {len(separa[0])} letras")