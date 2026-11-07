#4. Receba nome, peso e altura. Calcule IMC.


#Entrada
Nome = input("Digite seu nome: ")
Peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

#Processamento
imc = Peso / altura * 2

#Saida
print(f"Seu IMC é: {imc}")