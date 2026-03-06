#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input("Qual o sálario do funcionário? "))
aumento = salario + (salario * 0.15)
print(f"Sálario original: {salario}\n"
      f"Novo Sálario: {aumento}")