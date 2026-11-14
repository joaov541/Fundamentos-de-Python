#8) Faça um programa que receba o nome, cargo e salário de um funcionário. Se o
#funcionário ganhar abaixo de 1000 reais, calcule o salário acrescido de 10%. Ao final
#exiba o nome, o cargo e o salário desse funcionário.

nome = input("Digite seu nome: ")
cargo = input("Digite seu cargo: ")
salario = float(input("Digite seu salário: "))
salarioAcrecido = salario * 1.10

if salario < 1000: 
    print(f"Seu nomé é: {nome}")
    print(f"Seu cargo é: {cargo}")
    print(f"Seu salário acrecido de 10% é: {salarioAcrecido:.2f}")
else :
     print(f"Seu nomé é: {nome}")
     print(f"Seu cargo é: {cargo}")
     print(f"Seu salário é de: {salario:.2f}R$")