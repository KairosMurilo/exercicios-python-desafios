#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians
angulo = int(input("Digite o valor do ângulo: "))
print(f"Cosseno de {angulo}: {cos(radians(angulo)):.2f}\n"
      f"Seno de {angulo}: {sin(radians(angulo)):.2f}\n"
      f"Tangente de {angulo}: {tan(radians(angulo)):.2f}")