#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

from mypy.typeops import true_only

print("Vou pensar em um número entre 0 e 5, tente adivinhar qual número estou pensando!")
n1 = randint(0,5)
n2 = int(input("Digite aqui seu palpite: "))
acertou = False
palpites = 1

print("-=-" * 20)
print("PROCESSANDO...")
print("-=-" * 20)
sleep(2)

while not acertou:
    print(f"Você errou... tente acertar novamente:")
    n2 = int(input("Digite aqui seu palpite: "))
    palpites +=1
    if n2 == n1:
        acertou = True

print(f"Você acertou! eu pensei em {n1} e você palpitou {n2}, tudo isso em {palpites} palpites")





