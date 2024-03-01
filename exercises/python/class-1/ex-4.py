
# Faça um programa que calcule o aumento de um salário.
# Ele deve receber o valor do salário e o percentual 
# do aumento.Exiba o valor do aumento e o novo salário.

salario = float(input('Digite o valor do seu salário: R$'))
percentual = float(input('Digite o percentual do seu aumento: '))

novo_salario = salario + (salario * percentual / 100)

print('O valor do seu aumento é de R${:.2f}'.format(novo_salario))
print('O valor do seu novo salário é de R${:.2f}'.format(novo_salario))

