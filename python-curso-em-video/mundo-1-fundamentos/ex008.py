#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
num = float(input("Digite um valor em metros:"))
print("Valor em:\nMetros: {}".format(num))
print("Centímetros: {}".format(num*100))
print("Milímetros: {}".format(num*1000))