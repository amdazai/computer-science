
# Imprimir na tela todos os nomes da lista que tenham no máximo
# 5 letras. Interrompendo a listagem quando encontrar o nome “Maria”.

nomes = ["Joao", "Pedro", "José", "Silva", "Sofia", "Anna", "Maria"]

print ("início")

for nome in nomes:
    if len(nome) > 5:
        continue
    print ("Olá",nome)

    if nome == "Maria":
        break

print ("Fim")