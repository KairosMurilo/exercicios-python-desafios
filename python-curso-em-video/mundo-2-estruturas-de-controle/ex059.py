#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
menu = 0
while menu != 5:

    print("-=-" * 20)
    print("[Menu]\n"
          "[ 1 ] somar\n"
          "[ 2 ] multiplicar\n"
          "[ 3 ] maior\n"
          "[ 4 ] novos números\n"
          "[ 5 ] sair do programa\n")
    menu = int(input("Digite qual a opção escolhida: "))
    print("-=-" * 20)

    if menu == 1:
        soma = n1 + n2
        print (f"{n1} + {n2} = {soma}")
    elif menu == 2:
        soma = n1 * n2
        print(f"{n1} x {n2} = {soma}")
    elif menu == 3:
        if n1 > n2:
            print(f"{n1} é maior que {n2}")
        elif n1 == n2:
            print(f"{n1} é igual a {n2}")
        else:
            print(f"{n2} é maior que {n1}")
    elif menu == 4:
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o segundo valor: "))
    elif menu == 5:
        print("Encerrando o programa...")
    else:
        print("Opção inválida, digite novamente")