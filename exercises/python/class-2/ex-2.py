
# Escreva um programa que leia três números 
# e imprima o maior e o menor.

a = int(input("Digite o primeiro nº: "))
b = int(input("Digite o segundo  nº: "))
c = int(input("Digite o terceiro nº: "))

maior = a

if b > a and b > c:
    maior = b

if c > a and c > b:
    maior = c

print (f"O maior n é{maior}")

menor = a

if b < a and b < c:
    menor = b

if c < a and c < b:
    menor = c

print (f"O menor n é {menor}")