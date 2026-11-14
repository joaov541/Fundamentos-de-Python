#1. Receba a idade em anos e imprima em meses, dias, horas e minutos.

#Padrões de escria e variáveis, funções e etc em programação



#numeros, textos e booleanos
#Entrada
idade = int(input("Digite a idade: ")) #Pega o texto e converte para número

# Processamento
idadeEmMeses = idade * 12
idadeEmDias = idade * 365
idadeEmHoras = idadeEmDias * 24
idadeEmMinutos = idadeEmHoras * 60

#Saída
print(f"Sua idade em meses é: {idadeEmMeses} Meses")
print(f"Sua idade em dias é: {idadeEmDias} Dias")
print(f"Sua idade em horas é: {idadeEmHoras} Horas")
print(f"Sua idade em minutos é: {idadeEmMinutos} Minutos")
