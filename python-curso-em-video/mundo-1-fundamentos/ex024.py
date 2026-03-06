#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input("digite o nome uma cidade: ")).strip()
print(cidade[:6].lower() == "santo ")
