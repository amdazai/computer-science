
# Escreva um programa que pergunte o salário
# do funcionário e calcule o valor do aumento. 
# Para salários superiores a 1_250.00 BRL o 
# aumento será de 10%. Para os inferiores ou iguais de 15%

salário = float(input("Qual o seu salário? R$"))

if salário > 1250:
    print(f"Novo Salário é: {salário + (salário * 0.10 )}")

else:
    print(f"Novo Salário é: {salário + (salário * 0.15 )}")