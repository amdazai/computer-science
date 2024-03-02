
# Escreva um programa para aprovar o empréstimo bancário para comprar de uma casa. 
# O programa deve perguntar o valor da casa, o salário e a qualtidade de anos a pagar. 
# O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor 
# da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

casa = float(input("Qual o valor da casa? R$"))
salario = float(input("Qual o seu salário? R$"))
anos = int(input("Quantos anos pretende pagar?"))

prestacao = casa / (anos * 12)  

if prestacao > salario * 0.3:
    print("Infelizmente você não poderá realizar o empréstimo")
else:
    print("Parabens, Você poderá realizar o empréstimo !!")
    print(f"Você pagará prestações de R${prestacao:7.2f} por {anos} anos")
