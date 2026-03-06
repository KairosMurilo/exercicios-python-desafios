#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#IMC abaixo de 18,5: Abaixo do Peso
#Entre 18,5 e 25: Peso Ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade Mórbida
altura = float(input("Digite a sua altura (ex.: 1,70): "))
peso = float(input("Digite o seu peso (ex.: 69,2)"))
imc = peso / altura ** 2

if 18.5 <= imc < 25:
    print("Você está no peso ideal")
elif 25 <= imc < 30:
    print("Você está com Sobrepeso")
elif 30 <= imc < 40:
    print("Você está com Obesidade")
elif 40 < imc:
    print("Você está com Obesidade Mórbida")
else:
    print("Você está abaixo do peso ideal")