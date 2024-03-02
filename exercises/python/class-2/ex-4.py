
# Escreva um programa que pergunte a distância 
# que deseja percorrer em KM. Calcule o preço 
# da passagem, cobrando 0,50 BRL por KM para viagens 
# de até 200 KM, e 0,45 BRL para viagens mais longas.

distancia = float(input("Digite a distância a percorrer:"))

if distancia <= 200:
    passagem = (distancia * 0.5)

else:
    passagem = (distancia * 0.45)

print (f"O preço da passagem em R$ {passagem:7.2f}")
