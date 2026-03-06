#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
aux_media = 0
aux_idade = 0
aux_nome = ""
cont = 0

for i in range(4):
    nome = str(input(f"Digite o {i+1}º nome: "))
    idade = int(input(f"Digite a {i+1}º idade: "))
    sexo = str(input(f"Digite a {i+1}º sexo (H ou M): ")).upper()
    print("===//=== \n")

    aux_media += idade

    if sexo == "H":
        if idade > aux_idade:
            aux_idade = idade
            aux_nome = nome

    if idade < 20 and sexo == "M":
        cont += 1

media = aux_media/4

print(f"Média de idade do grupo: {media}")
print(f"Homem mais velho do grupo: {aux_nome}")
print(f"Número de mulheres com menos de 20 anos: {cont}")
