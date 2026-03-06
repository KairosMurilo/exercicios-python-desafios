#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
aux = termo + (10-1) * razao

i = termo
while i < aux:
    print (i)
    i += razao
