
# Escreva um programa que leia a quantidade de
# dias, horas, minutos e segundos do usuário. 
# Calcule o total em segundos e exiba o resultado na tela.

dia = int(input("Digite a quantidade de dias: "))
hora = int(input("Digite a quantidade de horas: "))
minuto = int(input("Digite a quantidade de minutos: "))
segundo = int(input("Digite a quantidade de segundos: "))

total = dia * 24 * 60 * 60 + hora * 60 * 60 + minuto * 60 + segundo 

print(f"O total de {dia} dias, {hora} horas, {minuto} minutos e {segundo} segundos é igual a {total} segundos.")