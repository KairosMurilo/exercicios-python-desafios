#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input("Digite uma frase: ")).strip()
print(f"A letra 'A' aparece {frase.lower().count("a")} vezes na frase")
print(f"A letra 'A' aparece a primeira vez na {frase.lower().find("a")+1}° posição")
print(f"A letra 'A' aparece a última vez na {frase.lower().rfind("a")+1}° posição")