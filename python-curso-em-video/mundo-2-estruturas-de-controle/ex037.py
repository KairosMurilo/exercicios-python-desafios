#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.
print("Qual será a base da conversão: \n"
      "[1]: Binário\n"
      "[2]: Octal\n"
      "[3]: Hexadecimal")
escolha = int(input("Sua escolha: "))
num = int(input("Agora digite qual o número que será convertido: "))
if escolha == 1:
    print(f"{num} convertido para binário é {bin(num)}")
elif escolha == 2:
    print(f"{num} convertido para Octal é {oct(num)}")
elif escolha == 3:
    print(f"{num} convertido para Hexadecimal {hex(num)}")
else:
    print("Escolha inválida. Tente novamente.")