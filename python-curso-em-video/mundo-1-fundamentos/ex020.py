#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle

lista = []
for i in range(4):
    nome = str(input(f"Digite o nome do {i+1}º aluno: "))
    lista.append(nome)
shuffle(lista)
print(f"a ordem será: \n"
      f"{lista}")
