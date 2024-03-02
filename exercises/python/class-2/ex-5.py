
# Escreva um programa que leia dois números e que 
# pergunte qual operação você deseja realizar. Você
# deve poder calcular soma (+), subtração (-), multiplicação 
# (*) e divisão (/). Exiba o resultado da operação solicitada.

a = int(input("Digite o primeiro número:"))
b = int(input("Digite o segundo número:"))

operação = input ("digite a operação ( +, -, * ou / ) :")

def new_func(a, b):
    print (a / b)

if operação == "+": 
    print (a + b)

elif operação == "-":
    print (a - b)

elif operação == "*":
    print (a * b)

elif operação == "/":
  if b > 0:
    print(a / b)

  else:
    print ("erro - divisão por zero")

else:
    print ("Operação invalida")