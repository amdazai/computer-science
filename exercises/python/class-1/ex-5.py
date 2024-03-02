
# Faça um programa que solicite o preço de uma mercadoria e o 
# percentual de desconto. Exiba o valor do desconto e o preço a pagar na tela

preco = float(input("Digite o preço da mercadoria: R$"))
desconto = float(input("Digite o percentual de desconto: "))

desconto = desconto / 100

preco = preco - (preco * desconto)

print(f"O valor do desconto é de R${desconto:.2f}")
print(f"O valor a pagar é de R${preco:.2f}") 