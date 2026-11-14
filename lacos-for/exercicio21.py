#21) Faça um programa que receba 15 números inteiros e imprima na tela
#a somatória dos 15 números.

total = 0

for i in range(1, 4):
    n = int(input("Digite um número: "))
    total = total + n
    
print(f"Soma total: {total}")