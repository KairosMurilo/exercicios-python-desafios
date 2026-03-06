#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))

contador = 0
mais = 10

while mais != 0:
    total = contador + mais

    while contador < total:
        print(termo)
        termo += razao
        contador += 1

    mais = int(input("Quantos termos você gostaria de visualizar a mais? "))

print("Progressão finalizada.")