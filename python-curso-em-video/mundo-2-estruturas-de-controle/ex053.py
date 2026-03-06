#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
#APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
texto = input("Digite uma frase: ")
texto2 = ""
for i in range(len(texto)-1, -1, -1):
    texto2 = texto2 + texto[i]

if texto.replace(" ", "").upper() == texto2.replace(" ", "").upper():
    print("É palindromo")
else:
    print("Não é palindromo")