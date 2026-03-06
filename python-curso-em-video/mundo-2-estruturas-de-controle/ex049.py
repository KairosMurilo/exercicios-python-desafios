#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
num = int(input("Digite o número que você queira descobrir a tabuada: "))
for i in range(1, 10, 1):
    print(f"{num} x {i} = {num * i}")