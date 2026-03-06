# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input("Qual velocidade do carro em Km/h? "))
multa = 0
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f"Você foi multado no valor de R${multa:.2f} por excesso de velocidade")
else:
    print("Carro dentro do limite de velocidade permitido")