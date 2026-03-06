# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes

a = float(input("Primeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmento: "))
if a < b + c and b < a + c and c < a + b:
    print("Os segmentos acima PODEM FORMAR um triângulo")
    if a == b == c:
        print("EQUILÁTERO.")
    elif a != b and b != c and a != c:
        print("ESCALENO.")
    else:
        print("ISÓSCELES.")
else:
    print("Os segmentos acima NÃO PODEM FORMAR um triângulo.")