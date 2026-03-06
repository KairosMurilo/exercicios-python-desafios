#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
distancia = int(input("Qual a distância da sua viagem em KM? "))
preco = 0
if distancia <= 200:
    preco = 0.50 * distancia
    print(f"A passagem custará R${preco:.2f}")
else:
    preco = 0.45 * distancia
    print(f"A passagem custará R${preco:.2f}")
