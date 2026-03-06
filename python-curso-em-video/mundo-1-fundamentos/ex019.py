#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
from random import choice

lista = []
for i in range (4):
    nome = str(input(f"Nome do {i+1}º aluno: "))
    lista.append(nome)
escolhido = choice(lista)
print(f"O aluno escolhido foi: {escolhido}")
