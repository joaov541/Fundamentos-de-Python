#12) Faça um programa que receba um número do usuário e informe se este número é
#par ou ímpar.

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")