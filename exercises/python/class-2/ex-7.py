
# Escreva um programa que recebe o nome do aluno(a) e suas 
# notas (N1 e N2) e calcula a média semestral (média aritméticadas 2 notas), 
# testa se o aluno(a) foi aprovado (média maior que 7.0).
# Ao final imprima: nome, N1, N2 e média.

nome = input("Digite seu nome:")
n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota:"))

media = (n1 + n2) / 2

if media >= 7:
    print("O aluno(a) foi aprovado!")
    print(f"A média do aluno(a) {nome} foi {media:.1f}")

if media < 7:
    print("O aluno(a) foi reprovado!")
    print(f"O aluno {nome} com as notas: {n1} e {n2} teve a média de {media:.1f}")