#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Digite aqui o seu sálario: "))
if salario <= 1250:
    novo_salario = salario + (salario * 0.15)
else:
    novo_salario = salario + (salario * 0.10)

print(f"Agora você receberá R${novo_salario:.2f} e antes recebia R${salario:.2f}")