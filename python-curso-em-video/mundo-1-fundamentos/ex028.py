#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep

print("Vou pensar em um número entre 0 e 5, tente adivinhar qual número estou pensando!")
n1 = randint(0,5)
n2 = int(input("Digite aqui seu palpite: "))

print("-=-" * 20)
print("PROCESSANDO...")
print("-=-" * 20)
sleep(2)

if n2 == n1:
    print(f"Você acertou! eu pensei em {n1} e você palpitou {n2}")
else:
    print(f"Você errou... eu pensei em {n1} e você palpitou {n2}")
