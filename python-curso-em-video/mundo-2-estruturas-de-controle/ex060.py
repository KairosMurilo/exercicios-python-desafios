#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
#5! = 5 x 4 x 3 x 2 x 1 = 120
n1 = int(input("Digite o número que deseja saber o fatorial: "))
i = 1
fatorial = 1
while i <= n1:
    fatorial *= i
    i += 1

print(f"Fatorial de {n1} = {fatorial} ")


