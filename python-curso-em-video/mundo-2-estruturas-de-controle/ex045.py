#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint

print("==[PEDRA, PAPEL, TESOURA]== \n"
      "[1]: Pedra\n"
      "[2]: Papel\n"
      "[3]: Tesoura")


p1 = int(input("Sua escolha: "))
p2 = randint(1, 3)


if p2 == 1:
    print("A máquina escolheu Pedra\n")
elif p2 == 2:
    print("A máquina escolheu Papel\n")
else:
    print("A máquina escolheu Tesoura\n")



if p1 == 1:
    if p2 == 1:
        print("Pedra x Pedra, Empate!")
    elif p2 == 2:
        print("Pedra x Papel, Você Perdeu!")
    else:
        print("Pedra x Tesoura, Você Venceu!")
elif p1 == 2:
    if p2 == 1:
        print("Papel x Pedra, Você Venceu!")
    elif p2 == 2:
        print("Papel x Papel, Empate!")
    else:
        print("Papel x Tesoura, Você Perdeu!")
elif p1 == 3:
   if p2 == 1:
       print("Tesoura x Pedra, você Perdeu!")
   elif p2 == 2:
       print("Tesoura x Papel, você Venceu!")
   else:
       print("Tesoura x Tesoura, Empate!")
else:
    print("Erro. Jogada inválida")