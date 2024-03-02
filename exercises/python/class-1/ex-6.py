
# Escreva um programa que pergunte a quantidade de KM percorridos
# por um carro alugado pelo usuário, assim como a quantidade de
# dias pelos quais o carro foi alugado. Calcule o preço a pagar, 
# sabendo que o carro custa 60 BRL por dia e 0,15 BRL por KM rodado.

km = float(input('Quantos KM foram percorridos? '))
dias = int(input('Quantos dias foi o carro alugado? '))

preco = (60 * dias) + (0.15 * km)

print(f'O preço a pagar é de R${preco:.2f}')
