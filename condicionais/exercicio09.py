#9) Uma empresa decide dar aumento de 30% aos funcionários cujo salário é inferior a
#500 reais. Escreva um programa que receba o salário de um funcionário e imprima o
#valor do salário reajustado ou uma mensagem caso o funcionário não tenha direito a
#aumento.

#aumento
print()
print()
print("|*******************************|")
print("|       PROGRAMA REAJUSTE       |")
print("|          VERSÃO 1.0           |")
print("|*******************************|")
print()
print()

salario = float(input("Digite seu salário: "))
salarioReajuste = salario * 1.30

if salario < 500: 
    print(f"Seu salario acrescido de 30% é de: R${salarioReajuste:.2f}")
else:
    print(f"Seu salário é de: {salario:.2f}")
    