# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Digite o salário: "))
novo_salario = salario + (salario * 0.15)

print(f"Salário atualizado: R${novo_salario:.2f}")
