# Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
#Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input("Digite o seu Sexo: [M/F]")).upper().strip()
while sexo not in 'MF':
    print("Valor Inválido!")
    sexo = str(input("Digite o seu Sexo: [M/F]")).upper()
print ("Sexo cadastrado com sucesso")