
# Escreva um programa que leia um valor em metros 
# e o exiba convertido em milímetros.

metros = int(input("Digite o valor em metros: "))

# para converter metros - cm se multiplica por 100 !

centimetros = metros * 100

print(f"O valor {metros}m em centímetros é {centimetros:.0f}cm")