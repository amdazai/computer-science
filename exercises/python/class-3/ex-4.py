
# Imprimir os números até um número (intervalo) máximo
# informado, indicado se são pares ou impares.

n = int(input("Informe o intervalo máximo:"))
for num in range(0, n):
    if num % 2 == 0:
        print(num, 'é par')
        continue
    print(num, "é impar")