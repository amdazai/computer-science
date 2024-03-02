
# Faça um programa recebe duas strings: (i) uma frase e (ii) uma letra. 
# Verifique e informe quantas vezes a letra aparece na frase.

fr = input("Digite a frase: ")
le = input("Digite a letra: ")

qtde_le = 0

for caracter in fr:
    if caracter.lower() == le.lower():
        qtde_le += 1

print (f'"Na frase "{fr}" existem ({qtde_le}) letras "{le}"')